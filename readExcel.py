# importing the xlrd module
import xlrd
# writing the path of the file
file = r"C:\Users\ezeki\Desktop\Tech Journey\PythonBootcamp\hello_tpoint_tech.xls"
# Open workbook
wb = xlrd.open_workbook(file)

# Select first sheet
sheet = wb.sheet_by_index(0)

# Get value at row 0, column 1
cell_value = sheet.cell_value(0, 1)
# printing the value from the excel sheet
print(cell_value)