from openpyxl import Workbook, load_workbook

# Load the excel workbook and store into wb
wb = load_workbook("input_day01.xlsx")

# Store the current excel worksheet into ws
ws = wb.active

# Create a list to store all the input values from excel as integers
input_list = []

for cell in ws.rows:
    input_list.append(cell[0].value)

# Create counter to count number of time depth increases
counter = 0

# Iterate through the list (len(list) - 3) times and compare two consecutive
# elements with each iteration
for i in range(len(input_list) - 3):
    if sum(input_list[i+1:i+4]) > sum(input_list[i:i+3]):
        counter += 1

print(counter)
