# import pandas as pd

# export = pd.read_excel('testlist.xlsx', header=None)
# mylist = ['{}'.format(item) for item in export.iloc[:, 0]]
# print(mylist)

# import pandas as pd

# # Read the Excel file into a DataFrame, treating the first column as strings
# export = pd.read_excel('testlist.xlsx', header=None, dtype=str)

# # Create a list of strings from the first column of the DataFrame
# mylist = [str(item) for item in export.iloc[:, 0]]

# # Print the list
# print(mylist)


# import pandas as pd

# # Read the Excel file into a DataFrame, treating the first column as strings
# export = pd.read_excel('testlist.xlsx', header=None, dtype=str)

# # Create a list of strings from the first column of the DataFrame
# mylist = [str(item) for item in export.iloc[:, 0]]

# # Write the list to a text file in list format
# with open('output.txt', 'w') as f:
#     f.write(str(mylist))


# import pandas as pd

# # Read the Excel file into a DataFrame, treating the first column as strings
# export = pd.read_excel('testlist.xlsx', header=None, dtype=str)

# # Create a list of strings from the first column of the DataFrame
# mylist = [str(item) for item in export.iloc[:, 0]]

# # Verify the length of the list
# print(f"Total items in the list: {len(mylist)}")

# # Write the list to a text file in list format
# with open('output.txt', 'w') as f:
#     f.write("[\n")
#     for item in mylist:
#         f.write(f"    '{item}',\n")
#     f.write("]\n")


import pandas as pd

# Read the Excel file into a DataFrame, treating the first column as strings
export = pd.read_excel('testlist.xlsx', header=None, dtype=str)

# Create a list of strings from the first column of the DataFrame
mylist = [str(item) for item in export.iloc[:, 0]]

# Write the list to a text file with 10 items per row
with open('output.txt', 'w') as f:
    f.write("[\n")
    for i in range(0, len(mylist), 10):
        # Join 10 items with commas and add a newline at the end
        items = ", ".join(f"'{item}'" for item in mylist[i:i+10])
        f.write(f"    {items},\n")
    f.write("]\n")
