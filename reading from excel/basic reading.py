# This comes from
# https://www.youtube.com/watch?v=p0DNcTnreuY

import xlrd
import datetime

file_location = "D:/Kody/Testing/Data Driven Testing/reading from excel/basic_reading.xlsx"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)

value = sheet.cell_value(0, 0)


rows_number = sheet.nrows
col_number = sheet.ncols


def print_column_values(rows):
    for row in range(1, rows):
        print(sheet.cell_value(row, 0))


def print_rows_values(cols):
    for col in range(0, cols):
        print(sheet.cell_value(1, col))

# Below method will work only if date of birth is a string / excel text date?
# Shortly it needs date in string format dd/mm/yy
def print_person_data():
    for col in range(col_number):
        cell_value = sheet.cell_value(1, col)
        if type(cell_value) == float:
            print(int(cell_value))
        elif '/' in cell_value:
            date = cell_value.split('/')
            day = date[0]
            month = date[1]
            year = date[2]
            if int(year) > 17:
                century_year = 19
            else:
                century_year = 20
            print("Day: %s, Month: %s, Year %d%s" % (day, month, int(century_year), year))
        else:
            print(cell_value)

#print_person_data()

def data_list():
    data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]
    return data
