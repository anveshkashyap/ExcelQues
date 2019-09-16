import xlrd

wb = xlrd.open_workbook("C:/Users/acer/PycharmProjects/ExcelQues/data/Category.xlsx")
ws = wb.sheet_by_name("Sheet1")
row_count = ws.nrows
col_count = ws.ncols


def get_header(input_val):
    for i in range(row_count):
        for j in range(col_count):
            if ws.cell_value(i, j).lower().strip() == input_val:
                print("The header of column is : ", ws.cell_value(0, j))
                break



input_val = input("Enter the value to get the corresponding header: ").lower().strip()
get_header(input_val)
