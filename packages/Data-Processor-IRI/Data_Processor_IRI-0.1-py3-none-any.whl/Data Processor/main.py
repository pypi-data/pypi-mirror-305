# main.py in Data Processor

import os
import nbformat
import logging
import asyncio
from flask import Flask, request, jsonify, render_template, send_from_directory, url_for
from nbconvert.preprocessors import ExecutePreprocessor
from flask_cors import CORS
import time
import pandas as pd
import glob
import shutil
import xlwings as xw
import re

# Set the event loop policy for Windows
if os.name == 'nt':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# Define the create_app function
def create_app():
    app = Flask(__name__)
    CORS(app)  # Enable CORS

    UPLOAD_FOLDER = os.path.join(os.getcwd(), "OUTPUT")
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    # Set up logging
    logging.basicConfig(level=logging.DEBUG)

    @app.route('/')
    def index():
        return render_template("index.html")

    @app.route('/upload', methods=['POST'])
    def upload_file():
        start_time = time.time()
        logging.debug("Received upload request")
        if 'file' not in request.files:
            logging.error("No file part in the request")
            return jsonify(success=False, error="No file part")

        file = request.files['file']
        if file.filename == '':
            logging.error("No selected file")
            return jsonify(success=False, error="No selected file")

        try:
            # Save the file to the upload folder
            file_path = os.path.join(UPLOAD_FOLDER, file.filename)
            logging.debug(f"Saving file to {file_path}")
            file.save(file_path)
            logging.debug(f"File saved to {file_path}")

            # Run the notebook with the file_path
            notebook_path = os.path.join(os.getcwd(), "IRI PHASE_3_final_copy.ipynb")
            logging.debug(f"Running notebook {notebook_path} with input file {file_path}")
            run_notebook(notebook_path, file_path)
            end_time = time.time()
            print("----------------------------------", start_time - end_time, "----------------------------------")
            return jsonify(success=True)
        except Exception as e:
            logging.error(f"Error processing file: {e}")
            return jsonify(success=False, error=str(e))

    def run_notebook(notebook_path, input_path):
        try:
            with open(notebook_path) as f:
                nb = nbformat.read(f, as_version=4)

            # Overwrite the file_path variable in the notebook
            variable_found = False
            for cell in nb.cells:
                if cell.cell_type == 'code' and 'file_path =' in cell.source:
                    cell.source = f"file_path = r'{input_path}'"
                    variable_found = True
                    break

            if not variable_found:
                nb.cells.insert(0, nbformat.v4.new_code_cell(f"file_path = r'{input_path}'"))

            # Execute the notebook
            ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
            ep.preprocess(nb, {'metadata': {'path': os.path.dirname(notebook_path)}})

        except SystemExit as e:
            logging.error(f"SystemExit caught: {e}")
            return jsonify(success=False, message="An error occurred during notebook execution. Please check the file list for details.", link=url_for('file_list'))

        except Exception as e:
            logging.error(f"Error running notebook: {e}")
            return jsonify(success=False, message="An unexpected error occurred while running the notebook.")

        logging.info("Backend is running properly after handling SystemExit.")
        return jsonify(success=True, message="Notebook executed successfully.")

    @app.route('/file_list')
    def file_list():
        try:
            files = os.listdir(UPLOAD_FOLDER)
            file_urls = [url_for('uploaded_file', filename=file) for file in files]
            return render_template('file_list.html', files=file_urls)
        except Exception as e:
            return jsonify(success=False, message=str(e))

    @app.route('/uploads/<filename>')
    def uploaded_file(filename):
        return send_from_directory(UPLOAD_FOLDER, filename)

    @app.route('/exception')
    def exception():
        return render_template('exception.html')

    @app.route('/save_table', methods=['POST', 'GET'])
    def save_table():
        edited_data = request.json
        df = pd.DataFrame(edited_data)

        df = df[["KEYCAT", "PLACEMENT", "NOTES"]]

        implementation_directory = r"Implementation File"
        impl_files = os.listdir(implementation_directory)
        xlsm_files = [file for file in impl_files if file.startswith(request.args.get('arg')) and file.endswith('.xlsm')]

        if xlsm_files:
            xlsm_file_path = os.path.join(implementation_directory, xlsm_files[0])
            os.makedirs(os.path.join(os.getcwd(), "BACKUP"), exist_ok=True)
            backup_path = os.path.join(r"BACKUP", "backup_" + xlsm_files[0])
            shutil.copyfile(xlsm_file_path, backup_path)

            with xw.App(visible=False) as app:
                wb = app.books.open(xlsm_file_path)

                sheet_names = [sheet.name.strip() for sheet in wb.sheets]

                if 'RECAP_OLD' in sheet_names:
                    recap_sheet = 'RECAP_OLD'
                elif 'RECAP' in sheet_names:
                    recap_sheet = 'RECAP'
                else:
                    return jsonify({'error': 'Neither RECAP_OLD nor RECAP sheet found'}), 400

                ws = wb.sheets[recap_sheet]

                recap_data = ws.range('A2').expand().value
                recap_data = [[int(row[0])] + row[1:] for row in recap_data if row[0].isdigit()]

                for _, row in df.iterrows():
                    keycat = row['KEYCAT']
                    placement = row['PLACEMENT']
                    notes = row['NOTES']

                    matched = False
                    for r_idx, r_data in enumerate(recap_data):
                        if r_data[2] == placement:
                            matched = True
                            ws.range(f"I{r_idx+2}").value = notes
                            break
                    if not matched:
                        print(f"No match found for KEYCAT={keycat}, PLACEMENT={placement}, NOTES={notes}")

                wb.save(xlsm_file_path)
                wb.close()

        return jsonify({'message': f'Changes made successfully'}), 200

    return app

if __name__ == '__main__':
    create_app().run(debug=True, use_reloader=False)
