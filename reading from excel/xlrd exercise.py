import xlrd


def open_file(path):

    # Open and read a Excel file
    workbook = xlrd.open_workbook(path)

    # print number of sheets
    sheets_number = workbook.nsheets
    print(sheets_number)

    # Print sheets' names
    sheets_names = workbook.sheet_names()
    print(sheets_names)

    # Get first worksheet
    first_sheet = workbook.sheet_by_index(0)

    # Read first row
    print(first_sheet.row_values(0))

    # Read a cell
    cell = first_sheet.cell(0, 0)
    print(cell)
    print(cell.value)

    # Read a row slice
    print(first_sheet.row_slice(rowx=1,
                                start_colx=0,
                                end_colx=3))


if __name__ == "__main__":
    path = './basic_reading.xlsx'
    open_file(path)

