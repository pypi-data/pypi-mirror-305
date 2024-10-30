#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd #pandas for dataframes and manipulation
import glob #To manage path
import os  #os functionalities
from openpyxl import Workbook
from openpyxl.styles import PatternFill


# In[2]:


file_path = r"C:\IRI\IRI ROM PLACEMENT_FINAL (2)\IRI ROM PLACEMENT_FINAL\Implementation File\WMT_9524_BAFOLICO_202410040633.xlsm"

# file_path=r"C:\IRI\IRI ROM PLACEMENT_FINAL (2)\IRI ROM PLACEMENT_FINAL\Implementation File\ALD_4006_SSCAPRTE_202409270510.xlsm"

# file_path=r"C:\IRI\IRI ROM PLACEMENT_FINAL (2)\IRI ROM PLACEMENT_FINAL\Implementation File\AMZ_0806_SSSALSA_202408010605.xlsm"

# file_path=r"C:\IRI\IRI ROM PLACEMENT_FINAL (2)\IRI ROM PLACEMENT_FINAL\Implementation File\SNK_7431_NLACSRIM_202408011119.xlsm"

# file_path=r"C:\IRI\IRI ROM PLACEMENT_FINAL (2)\IRI ROM PLACEMENT_FINAL\Implementation File\LDL_7020_ICEHTPCK_202408090604.xlsm"

# file_path="C:/IRI/IRI ROM PLACEMENT_FINAL (2)/IRI ROM PLACEMENT_FINAL/Implementation File/SNK_2613_DISDIALI_202408011038.xlsm"

# file_path="C:/IRI/IRI ROM PLACEMENT_FINAL (2)/IRI ROM PLACEMENT_FINAL/Implementation File/SNK_0117_EYELASH_202408011145.xlsm"

# file_path=r"C:\IRI\IRI ROM PLACEMENT_FINAL (2)\IRI ROM PLACEMENT_FINAL\Implementation File\SNK_7585_LICETREA_202408011016.xlsm"


# file_path="C:/IRI/IRI ROM PLACEMENT_FINAL (2)/IRI ROM PLACEMENT_FINAL/Implementation File/HTI_0843_SSMTSCEM_202408200805.xlsm"

# file_path=r"C:\IRI\IRI ROM PLACEMENT_FINAL (2)\IRI ROM PLACEMENT_FINAL\Implementation File\ALD_4006_SSCAPRTE_202409270510.xlsm"

# file_path=r"C:\IRI\IRI ROM PLACEMENT_FINAL (2)\IRI ROM PLACEMENT_FINAL\dummy\HTI_0843_SSMTSCEM_202408200805.xlsm"

# file_path = r"C:\Users\703364648\OneDrive - Genpact\Documents\New folder\IRI ROM PLACEMENT\Implementation File\AMZ_0843_SSMTSCEM_202405281059.xlsm"


# In[3]:


#staging file is created with the filled ROM items as there are no libraries to append on the xlsm file format
#the macro excel will copy the contents of the staging file to the original keycat file
staging_path = file_path.replace(".xlsm","_staging.xlsx")
error_on_comments_path = file_path.replace(".xlsm","_error_on_comments.xlsx")

'''staging_path_recap = file_path.replace(".xlsm","_staging_recap.xlsx")'''

#the probable mismatched placements are dumped into the *_mismatches file
mismatch_file_path = file_path.replace(".xlsm","_mismatches.xlsx")

if "ITEM_OLD" in pd.ExcelFile(file_path).sheet_names:
    item_sheet="ITEM_OLD"
else:
    item_sheet="ITEM"
 
if "RECAP_OLD" in pd.ExcelFile(file_path).sheet_names:
    recap_sheet="RECAP_OLD"
else:
    recap_sheet="RECAP"



# reading the item and recap tab
df_item = pd.read_excel(file_path, sheet_name=item_sheet, dtype=str)
df_recap = pd.read_excel(file_path, sheet_name=recap_sheet)
df_recap_copy2 = df_recap.copy(deep=True)


# In[4]:


df_recap = df_recap[df_recap["GYOR"].isin(["Y","G"])] #filter only green and yellow placements
df_recap = df_recap[~df_recap["NOTES"].str.contains("MULTIGEN")]    #remove multigen placements
df_recap = df_recap[~df_recap["NOTES"].str.contains("CLIENT WANTS")]    #remove client specific placements
df_recap_copy = df_recap.copy(deep=True)


# In[5]:


df_recap=df_recap[["PLACEMENT","NOTES"]]
df_recap


# In[7]:


import re
df_recap['Priority'] = df_recap['NOTES'].apply(lambda x: int(re.search(r'\[(\d+)\]', x).group(1)) if re.search(r'\[(\d+)\]', x) else None)


# In[8]:


df_recap


# In[9]:


df_recap_check = df_recap.copy(deep=True)
df_recap_check


# In[10]:


df_recap['NOTES'] = df_recap['NOTES'].str.replace(r'\[\d+\]\s*', '', regex=True)


# In[11]:


df_recap


# In[12]:


def find_bracket_indices(note):
    # Ignore everything from 'COMMENT' onwards
    # comment_index = note.find('COMMENT')
    # if comment_index != -1:
    #     note = note[:comment_index]

    stack = []
    indexes = []
    
    # Mapping of opening and closing brackets
    bracket_map = {
        '(': ')',
        '{': '}'
        
    }
    
    for i, ch in enumerate(note):
        if ch in bracket_map:  # If it's an opening bracket
            stack.append((ch, i))
        elif ch in bracket_map.values():  # If it's a closing bracket
            if stack:
                opening_bracket, opening_index = stack.pop()
                # Check if the closing bracket matches the last opening bracket
                if bracket_map[opening_bracket] == ch:
                    indexes.append([opening_index, i])
    
    return indexes




# In[13]:


def find_paretheses(note):
    start_index = []
    end_index = []
    indexes = []
    for i,ch in enumerate(note):
        if ch == "(":
            start_index.append(i)
        elif ch == ")":
            end_index.append(i)
    for i1,i2 in zip(start_index,end_index):
        indexes.append([i1,i2])
    return(indexes)


# In[14]:


def find_round_bracket_indices(n):
    indices = []
    stack = []
    length = len(n)  # Get the length of the string
 
    for i in range(length):
        char = n[i]  # Access the character at index i
        
        # Check if we can safely access n[i + 1]
        if char == '(' and (i < length - 1):  # Ensure i is not the last index
            x = n[i + 1]
            if x != '>' and x != '<':
                stack.append(i)  # Store the index of the opening bracket
        elif char == ')':
            if stack:
                start_index = stack.pop()  # Get the matching opening bracket index
                indices.append((start_index, i))  # Append the tuple of indices
 
    return indices


# In[15]:


def find_attributes(n, p):
    attr_values = [p]
    count = 0
    maxi = 0
    
    # Check for any attribute containing numerical ranges
    indices = find_bracket_indices(n)
 
    # print(indices)
 
    if '{' in n:
    
        for ind in indices:
            if n[ind[0]] == '{':  # Found the curly bracket
                attribute = n[ind[0] + 1:ind[1]].strip()
                # print("Attribute values are", attr_values)
                attr_values.append(attribute)  # Add the attribute
                count += 1
                maxi = max(count, maxi)
 
                # Get numerical values from round brackets
                round_brackets = find_paretheses(n)
                numerical_conditions = []
                
                for round_ind in round_brackets:
                    numerical_value = n[round_ind[0] + 1:round_ind[1]].strip()
                    if(numerical_value.startswith('>=') or numerical_value.startswith('<=') or numerical_value.startswith('>') or numerical_value.startswith('<')):
                        numerical_conditions.append(numerical_value)
 
                # Ensure the column specified by the attribute is numeric
                column_name = attribute  # Use the attribute name as the column name
                df_item[column_name] = pd.to_numeric(df_item[column_name], errors='coerce', downcast="float")
 
                # Initialize the filter mask
                mask = pd.Series([True] * len(df_item))
 
                # Process each numerical condition
                for condition in numerical_conditions:
                    cleaned_value = condition.lstrip('=<>')
                    # print("The values are",cleaned_value)
                    if cleaned_value.strip():  # Check if there's a number after cleaning
                        try:
                            if condition.startswith('>='):
                                range_start = float(cleaned_value)
                                mask &= (df_item[column_name] >= range_start)
                            elif condition.startswith('<='):
                                range_end = float(cleaned_value)
                                mask &= (df_item[column_name] <= range_end)
                            elif condition.startswith('>'):
                                range_start = float(cleaned_value)
                                mask &= (df_item[column_name] > range_start)
                            elif condition.startswith('<'):
                                range_end = float(cleaned_value)
                                mask &= (df_item[column_name] < range_end)
                        except ValueError:
                            continue  # Skip if conversion fails
 
                # Apply the combined mask to filter values
                filtered_values = df_item[mask][column_name].unique()
                # print("Filtered values are - ", filtered_values)
                if filtered_values.size > 0:
                    # print("Attribute values are", attr_values)
                    attr_values.append(','.join(map(str, filtered_values)))
                    # print("Attribute values are", attr_values)
                else:
                    attr_values.append("")  # No values found in range
 
                # print("Attribute values are", attr_values)
 
                break  # Exit after processing the first found attribute with a range
 
            elif (n[ind[0]-2]!='}'):
            # Use find_paretheses if not TOTAL_OUNCES
                indices = find_round_bracket_indices(n)
            
                for ind in indices:
                    attribute = ""
                    attribute_index = ind[0] - 1
                    
                    # Extract attribute name
                    while attribute_index >= 0 and n[attribute_index] == " ":
                        attribute_index -= 1
                    while attribute_index >= 0 and n[attribute_index] not in (" ", ";", ",", ".", ")", "]", "}"):
                        attribute += n[attribute_index]
                        attribute_index -= 1
                    
                    # Reverse the attribute string
                    attribute = attribute[::-1]
                    
                    # Extract numerical value
                    numerical_val = n[ind[0] + 1:ind[1]].strip()
                    # print("Attribute is", attribute)
                    attr_values.append(attribute)
                    count += 1
                    maxi = max(count, maxi)
                    attr_values.append(numerical_val)
 
    # Check for any attributes after "COMMENT"
        if "COMMENT" in n:
            comment_index = n.index("COMMENT")
            comment_part = n[comment_index:]  # Get everything after "COMMENT"
            comment_indices = find_paretheses(comment_part)  # Extract any attributes in parentheses
            
            for ind in comment_indices:
                attribute = ""
                attribute_index = ind[0] - 1
                
                # Extract attribute name
                while attribute_index >= 0 and comment_part[attribute_index] == " ":
                    attribute_index -= 1
                while attribute_index >= 0 and comment_part[attribute_index] not in (" ", ";", ",", ".", ")", "]", "}"):
 
                    attribute += comment_part[attribute_index]
                    attribute_index -= 1
                
                # Reverse the attribute string
                attribute = attribute[::-1]
                
                # Extract numerical value
                numerical_value = comment_part[ind[0] + 1:ind[1]].strip()
                attr_values.append(attribute)
                count += 1
                maxi = max(count, maxi)
                attr_values.append(numerical_value)
            
    else:
        # Use find_paretheses if not TOTAL_OUNCES
        indices = find_paretheses(n)
        
        for ind in indices:
            attribute = ""
            attribute_index = ind[0] - 1
            
            # Extract attribute name
            while attribute_index >= 0 and n[attribute_index] == " ":
                attribute_index -= 1
            while attribute_index >= 0 and n[attribute_index] not in (" ", ";", ",", ".", ")", "]", "}"):
 
                attribute += n[attribute_index]
                attribute_index -= 1
            
            # Reverse the attribute string
            attribute = attribute[::-1]
            
            # Extract numerical value
            numerical_val = n[ind[0] + 1:ind[1]].strip()
            attr_values.append(attribute)
            count += 1
            maxi = max(count, maxi)
            attr_values.append(numerical_val)
    
    return attr_values, maxi
 


# In[17]:


results=[]
for i in range(len(df_recap)):
    note = df_recap.iloc[i]["NOTES"] 
   
    row,maxi_count= find_attributes(note,df_recap.iloc[i]["PLACEMENT"])
    results.append(maxi_count)

# Extract the maximum count of attributes
max_overall = max(results)
print(max_overall)


# In[18]:


placement_columns = ["PLACEMENT"]
for i in range(1, max_overall + 1):
    placement_columns.append(f"A{i}")
    placement_columns.append(f"V{i}")


# In[19]:


placement_df = pd.DataFrame(columns=placement_columns)
placement_df


# In[20]:


col_count = placement_df.shape[1]
for i in range(len(df_recap)):
    print(df_recap.iloc[i]["PLACEMENT"])
    note = df_recap.iloc[i]["NOTES"] 
    row,_ = find_attributes(note,df_recap.iloc[i]["PLACEMENT"])
    if len(row) < col_count:
        row.extend([None] * (col_count-len(row))) #to match the no. of columns of the dataframe
    print(row)

    for i in range(2,col_count,2):
        cleaned_values = []
        if row[i] is not None:
            for s in row[i].split(','):
                ch = s.strip()
                if "*" in ch and len(ch)>1:
                    if ch[0] == "*":
                        while(ch[1] == " "):
                            ch = ch.replace(" ","",1)
                    if ch[-1] == "*":
                        while(ch[-2] == " "):
                            ch = ch.replace(" ","",1)
                cleaned_values.append(ch)
            row[i] = cleaned_values                                    
    placement_df.loc[len(placement_df)] = row


# In[21]:


placement_df


# In[22]:


# placement_df.to_excel("test2.xlsx", index=False)


# In[23]:


df_item.info()


# In[24]:


placement_df.info()


# In[25]:


df_recap_check


# In[26]:


df_recap


# In[27]:


import re

def check_placement_errors(df_recap,df_recapdf_recap_check, placement_df, max_overall, columns):
    error_list = []
    error_placements = set()

    # Check notes in df_recap
    for i in range(len(df_recap_check)):
        note = df_recap_check.iloc[i]["NOTES"]
        placement = df_recap.iloc[i]["PLACEMENT"]
        prior=df_recap.iloc[i]["Priority"]
        matches = re.findall(r'\[\d+\]', note)

        if pd.isna(prior):
            error_list.append([placement, "No Priority Given at Start"])
            error_placements.add(placement)
            
        # Check for standardization
        if len(matches) > 1:
            error_list.append([placement, "Multiple Priorties"])
            error_placements.add(placement)
            
    # Check attributes in placement_df
    for i in range(len(placement_df)):
        attribute_values = []
        placement = placement_df.iloc[i]['PLACEMENT']

        # Collect attribute values for the current row
        for j in range(1, max_overall + 1):
            attribute_col = f'A{j}'  # Generate column name (A1, A2, ...)
            if attribute_col in placement_df.columns:
                attribute_values.append(placement_df[attribute_col].iloc[i])  # Collect attribute value

        # Find duplicates among attributes
        duplicates = set()  # Use a set to track duplicates
        seen = set()  # To track seen attributes

        for attr in attribute_values:
            if attr is not None:
                if attr in seen:
                    duplicates.add(attr)  # Add to duplicates set
                else:
                    seen.add(attr)  # Mark this attribute as seen

        # Log duplicates
        if duplicates:
            error_list.append([placement, f"Duplicate Attributes: {list(duplicates)}"])
            error_placements.add(placement)
            

        # Check if attributes exist in columns
        for attr in seen:
            if attr not in columns:
                error_list.append([placement, f"{attr} Not Found"])
                error_placements.add(placement)
                

    # Print all errors
    df_error = pd.DataFrame(error_list,columns=["PLACEMENT", "COMMENTS ON ERROR"])

    return df_error




# In[28]:


columns = list(df_item.columns)


# In[29]:


df_error=check_placement_errors(df_recap,df_recap_check,placement_df,max_overall,columns)


# In[30]:


df_error


# In[31]:


concat_dict = {}
for name, group in df_error.groupby('PLACEMENT'):
    concat_dict[name] = ', '.join(group['COMMENTS ON ERROR'].tolist())


# In[32]:


result_df = pd.DataFrame(list(concat_dict.items()), columns=['PLACEMENT', 'COMMENTS ON ERROR'])
result_df


# In[33]:


import sys

if len(result_df) > 0:
    df_error_on_notes = df_recap_copy.merge(result_df, on="PLACEMENT", how="left")
    df_error_on_notes[df_error_on_notes["COMMENTS ON ERROR"].isna() == False][["KEYCAT","PLACEMENT","NOTES",         "COMMENTS ON ERROR"]].to_excel(error_on_comments_path, index = False)
    sys.exit()
        



# In[34]:


# Get all unique columns from placement_df dynamically
all_columns = set()
for col in placement_df.columns:
    if col.startswith('A'):  # Assuming columns of interest start with 'A'
        all_columns.update(set(placement_df[col].unique()))

# Fill NaN values in df_item for each unique attribute found
for i in all_columns:
    if i is not None:
        print(i)
        df_item[i] = df_item[i].fillna("#####")


# In[35]:


default_placement=None
for index, row in df_recap.iterrows():
    if '(*)' in row['NOTES'] or '(ALL)' in row['NOTES'] or '(*,)' in row['NOTES']:
        default_placement = row['PLACEMENT']
        break  # Stop after finding the first match
 
print(f"The default placement is: {default_placement}")


# In[36]:


# Iterate through rows and update placement_df
for index, row in placement_df.iterrows():
    for i in range(1, placement_df.shape[1] - 1, 2):  # Iterate through value columns
        if row.iloc[i] is not None:
            new_list = []
            val = row.iloc[i + 1]  # Access the corresponding value
            attribute = row.iloc[i]  # Get the attribute name
            
            # Ensure val is a list
            if not isinstance(val, list):
                val = [val]
            
            # Process each value in val
            for x in val:
                if x is None:
                    continue  # Skip if x is None

                # Transform "IS NOT" for each value
                if isinstance(x, str) and "IS NOT" in x:
                    x = x.replace("IS NOT", "<>").strip()

                # Apply filtering logic based on the transformed value
                if x == "*" or x == "ALL":
                    
                    new_list += df_item[attribute].tolist()
                if x.startswith("<>"):
                    # Exclusion cases
                    exclude_value = x[2:].strip()
                    if exclude_value.startswith('*') and exclude_value.endswith('*'):
                        pattern = exclude_value[1:-1]
                        new_list += df_item[~df_item[attribute].str.contains(pattern, na=False)][attribute].tolist()
                    elif exclude_value.startswith('*'):
                        exclude_value = exclude_value[1:].strip()
                        new_list += df_item[~df_item[attribute].str.startswith(exclude_value)][attribute].tolist()
                    elif exclude_value.endswith('*'):
                        exclude_value = exclude_value[:-1].strip()
                        new_list += df_item[~df_item[attribute].str.endswith(exclude_value)][attribute].tolist()
                    else:
                        new_list += df_item[df_item[attribute] != exclude_value][attribute].tolist()
                if not x.startswith("<>"):
                    # Ensure attribute column is treated as string
                    df_item[attribute] = df_item[attribute].astype(str)
                    
                    # Inclusion cases
                    if x.startswith('*') and x.endswith('*'):
                        pattern = x[1:-1]
                        new_list += df_item[df_item[attribute].str.contains(pattern, na=False)][attribute].tolist()
                    elif x.startswith('*'):
                        pattern = x[1:].strip()  # Ends with pattern
                        new_list += df_item[df_item[attribute].str.endswith(pattern)][attribute].tolist()
                    elif x.endswith('*'):
                        pattern = x[:-1].strip()  # Starts with pattern
                        new_list += df_item[df_item[attribute].str.startswith(pattern)][attribute].tolist()
                    else:
                        #  print(f"Including items in attribute {attribute} exactly matching '{x}'")
                        #  new_list += df_item[df_item[attribute].str.contains(r'\b' + re.escape(x) + r'\b', na=False)][attribute].tolist()

                        # Contains pattern
                        #new_list += df_item[df_item[attribute].str.contains(x, na=False)][attribute].tolist()
                       
                        new_list += df_item[df_item[attribute].str.contains(f"^{x}$", na=False)][attribute].tolist()


            # Remove duplicates
            new_list = list(set(new_list))

            # new_list = list(dict.fromkeys(new_list))

            # Log the new list before assignment
            print(f"New list for row {index}, attribute {attribute}: {new_list}")

            # Update the placement_df with the new list of values
            placement_df.at[index, f'V{(i + 1) // 2}'] = new_list

print("Updated placement_df:")
print(placement_df)



# In[37]:


placement_df


# In[38]:


df_recap.sort_values(by='Priority', ascending=True)


# In[39]:


final_df = pd.merge(df_recap[['PLACEMENT',"Priority"]], placement_df, on='PLACEMENT', how='inner')


# In[40]:


final_df


# In[41]:


placement_df_sorted = final_df.sort_values(by='Priority', ascending=True)
placement_df_sorted


# In[42]:


original_df_item_2 = df_item.copy()


if "ATTR" in pd.ExcelFile(file_path).sheet_names:
    attr_sheet="ATTR"


df_attr = pd.read_excel(file_path, sheet_name=attr_sheet)









# Create a dictionary for attribute priority
priority_dict = dict(zip(df_attr['ATTR_COLUMN_NAME'], df_attr['PRIORITY']))

# Define a function to concatenate attributes based on their priority
def concatenate_attributes(row):
    # Create a list to store attribute values with their priority
    prioritized_values = []

    # Loop through each attribute in the row
    for attr, priority in priority_dict.items():
        if attr in row and pd.notna(row[attr]):
            prioritized_values.append((priority, row[attr]))

    # Sort based on priority and concatenate
    prioritized_values.sort()  # Sort by the first element (priority)
    return '|'.join(value for _, value in prioritized_values)

# Apply the function to each row and update column K
original_df_item_2['CONCAT_ATTRS'] = original_df_item_2.apply(concatenate_attributes, axis=1)

# Check if the existing value in column K is empty and update accordingly
original_df_item_2['CONCAT_ATTRS'] = original_df_item_2.apply(
    lambda row: row['CONCAT_ATTRS'] if pd.isna(row['CONCAT_ATTRS']) or row['CONCAT_ATTRS'] == '' else row['CONCAT_ATTRS'],
    axis=1
)

# Display the updated DataFrame or process it as needed
print(original_df_item_2[['UPC', 'CONCAT_ATTRS']])  # Replace 'UPC' with the actual column name for UPC if different


# In[43]:


placement_df_sorted = placement_df_sorted.sort_values(by="Priority")
# Initialize lists for mismatches and matches
mismatches = []
matches = []
match_count = 0  # Initialize match counter

# Copy of the original df_item to avoid modifying it during iterations
original_df_item_1 = df_item.copy()


for index, row in placement_df_sorted.iterrows():
    # Create a dynamic list of attributes and values
    attributes = []
    values = []
    attribute_value_pairs = {}

    # Collect attributes and values dynamically
    for i in range(2, 2 + max_overall * 2, 2):
        attribute = row.iloc[i]
        value = row.iloc[i + 1]
        if attribute is not None and value is not None:
            attributes.append(attribute)
            values.append(value)
            attribute_value_pairs[attribute] = value

    # If attributes exist, apply them dynamically in the query
    if len(attributes) > 0:
        # Start with a True series to apply & operator
        filter_query = pd.Series([True] * len(original_df_item_1))
        for attr, val in zip(attributes, values):
            filter_query &= df_item[attr].isin(val)

        # Create a temporary DataFrame based on the filtered query
        temp_df = original_df_item_1[filter_query]
        print(f"Filtered {len(attributes)} attributes, temp_df size: {len(temp_df)}")

        # Fill 'NEW_PLACEMENT' where it is NaN with the current placement
        temp_df["NEW_PLACEMENT"].fillna(row.iloc[0], inplace=True)

        temp_df_2 = original_df_item_2[filter_query]

        # Check for mismatches
        mismatch_condition = (temp_df_2["NEW_PLACEMENT"] != row.iloc[0]) & (temp_df_2["SOURCE_NEW_PLACEMENT"] != "CLIENT")
        mismatched_items = temp_df_2[mismatch_condition]

        # If there are mismatches, log them
        # df_recap[df_recap["PLACEMENT"] == mismatch_row["NEW_PLACEMENT"]]["NOTES"].values.tolist()
        if not mismatched_items.empty:
            for _, mismatch_row in mismatched_items.iterrows():
                mismatches.append([
                    mismatch_row["UPC"],
                    mismatch_row["NEW_PLACEMENT"],
                    row.iloc[0],
                    mismatch_row["CONCAT_ATTRS"]
                ])
        else:
            # If no mismatches, we can count the matches
            match_condition = (temp_df_2["NEW_PLACEMENT"] == row.iloc[0]) & (temp_df_2["SOURCE_NEW_PLACEMENT"] != "CLIENT")
            matched_items = temp_df_2[match_condition]
            if not matched_items.empty:
                count = len(matched_items)
                match_count += count  # Increment the match counter
                matches += [row.iloc[0]] * count  # Log the matches

        # Remove all UPCs found in the filtered query from the original DataFrame
        original_df_item_2 = original_df_item_2[~original_df_item_2["UPC"].isin(temp_df["UPC"])]

        # Update df_item with the new placements only if there are no mismatches
        if mismatched_items.empty:
            df_item.update(temp_df)

# Convert mismatches to a DataFrame and save to a file
# mismatch_df = pd.DataFrame(mismatches, columns=["UPC", "PREVIOUS_PLACEMENT", "MATCHED_PLACEMENT", "PREVIOUS_PLACEMENT_ATTRIBUTE", "MATCHED_PLACEMENT_ATTRIBUTE"])

# Output results
print("Placement processing complete.")
print(f"Total mismatches: {len(mismatches)}")
print(f"Total matches: {len(matches)}")
print(f"Total matched count: {match_count}")  # Display the total count of matches


# In[44]:


#finally fill the default placements for those empty values which are not filled by the logic
if default_placement is not None:
    df_item["NEW_PLACEMENT"]=df_item['NEW_PLACEMENT'].fillna(default_placement)
#df_item.loc[df_item["NEW_PLACEMENT"].isna(), "NEW_PLACEMENT"] = default
df_item["NEW_PLACEMENT"].isna().sum()


# In[45]:


mismatches


# In[46]:


mismatches_df=pd.DataFrame(mismatches, columns=["UPC", "PREVIOUS_PLACEMENT", "MATCHED_PLACEMENT",  "MATCHED_PLACEMENT_ATTRIBUTE"])


# In[47]:


mismatches_df


# In[48]:


mismatches_df=mismatches_df.dropna(subset=['PREVIOUS_PLACEMENT'])


# In[49]:


mismatches_df


# In[50]:


mismatches_df.to_excel(mismatch_file_path, index=False,sheet_name="Mismatched_Placements")


# In[51]:


color_mapping = {
    "G": "92D050",  # Green
    "Y": "FFFF00",  # Yellow
    "R": "FF0000",  # Red
    "O": "FFC000"   # Orange
}


# In[52]:


with pd.ExcelWriter(mismatch_file_path, engine='openpyxl', mode='a') as writer:
    df_recap_copy2.to_excel(writer, index=False, sheet_name='Recap')
 
    # Get the workbook and the worksheet
    workbook = writer.book
    worksheet = writer.sheets['Recap']
 
    # Iterate through the rows in the worksheet
    for row in range(2, len(df_recap_copy2) + 2):  # Adjust for header row
        gyor_value = worksheet[f'H{row}'].value  # Assuming GYOR is in the 'H' column
        if gyor_value in color_mapping:
            fill_color = PatternFill(start_color=color_mapping[gyor_value], end_color=color_mapping[gyor_value], fill_type='solid')
            worksheet[f'H{row}'].fill = fill_color
 
    # Save the workbook after making changes
    workbook.save(mismatch_file_path)


# In[53]:


all_columns = set()
for col in placement_df.columns:
    if col.startswith('A'):  # Assuming columns of interest start with 'A'
        all_columns.update(set(placement_df[col].unique()))

# Fill NaN values in df_item for each unique attribute found
for i in all_columns:
    if i is not None:
        print(i)
        df_item[i] = df_item[i].fillna("#####")


# In[54]:


#the ROM filled item_df is dumped into excel
df_item.to_excel(staging_path,index=False)


# In[55]:


#dataframe for the macro to place the source sheet from the source file to the destination sheet in the destination macro file
path_map_df = pd.DataFrame({"Source Workbook":[staging_path],"Destination Workbook":[file_path],"Source_Sheet:":["Sheet1"],"Destination Sheet":[item_sheet]})
path_map_df


# In[56]:


#dump the file in the macro approach folder
# path_map_df.to_excel(r"C:\Users\703364648\OneDrive - Genpact\Desktop\IRI Automation\Macro Approach\parameter_values.xlsx",index=False)
path_map_df.to_excel(os.getcwd()+"\\Macro Approach\\parameter_values.xlsx",index=False)


# In[57]:


#macro file in excel takes copy from staging file and replaces it in original file. The openpyxl library cannot handle xlsm file
import os
import win32com.client
 
# Path to the file
path1 = os.path.abspath(os.getcwd()+"\\Macro Approach\\parameter_staging.xlsm")
 
# Start an instance of Excel
xl = win32com.client.DispatchEx("Excel.Application")
 
# Open the workbook in Excel
wb = xl.Workbooks.Open(path1)
 
# Run the macro
xl.Application.Run("parameterMacro")
xl.Application.Run("macroStaging")

# Save the workbook and close
wb.Save()
wb.Close()
 
# Quit Excel
xl.Quit()


# In[58]:


#delete the staging file
import os,glob
directory ="OUTPUT//"
pattern = os.path.join(directory, '*staging.xlsx')
files_to_delete = glob.glob(pattern)
print(files_to_delete)
for file_path in files_to_delete:
    try:
        print(file_path)
        os.remove(file_path)
        print(f"Deleted: {file_path}")
        
    except OSError as e:
        print(f"Error: {file_path} : {e.strerror}")


# In[ ]:




