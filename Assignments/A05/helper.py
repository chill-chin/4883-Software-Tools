## To make the data from 'dwarf_family_tree.csv' usable, following steps were taken:

# 1. Manually restrict number of entries to 56 (same as the size of other file)
# 2. Remove unnecessary fields: myear,	mage,	ptype
# 3. Use ChatGPT to generate 56 Mexican names and their corresponding data (Birth date, Death date and years lived, SpouseID and so on...)
# 4. Use Python to replace fields from the Mexican name file (mexican_names.csv) to dwarf_family_tree.csv
# 5. Use subprocess.run function in main.py to execute 'helper.py'

import csv 

# Read data from the first CSV file
data1 = []
with open('dwarf_family_tree.csv', 'r') as file1:
    reader1 = csv.reader(file1)
    for row in reader1:
        data1.append(row)

# Read data from the second CSV file
data2 = []
with open('mexican_names.csv', 'r') as file2:
    reader2 = csv.reader(file2)
    for row in reader2:
        data2.append(row)

# Replace the field in the first file with values from the second file
for i in range(len(data1)):
  data1[i][1] = data2[i][0]  # Sort Names
  data1[i][2] = data2[i][1]  # Sort Gender
  data1[i][3] = data2[i][3]  # Sort Generation
  data1[i][0] = data2[i][2]  # Sort PID
  data1[i][4] = data2[i][4]  # Sort Birth Year
  data1[i][5] = data2[i][5]  # Sort Death Year
  data1[i][6] = data2[i][6]  # Sort Age at Death
  data1[i][7] = data2[i][7]  # Sort Clans
  data1[i][8] = data2[i][8]  # Sort SpouseID
  data1[i][9] = data2[i][9]  # Sort Parent1ID
  data1[i][10] = data2[i][10]  # Sort Parent1ID

# Write the modified data back to the first file
with open('family_tree_data.csv', 'w', newline='') as file1:
    writer = csv.writer(file1)
    writer.writerows(data1)
