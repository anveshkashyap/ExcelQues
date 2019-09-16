import xlrd

wb = xlrd.open_workbook("C:/Users/acer/PycharmProjects/ExcelQues/data/Roaster.xlsx")
ws = wb.sheet_by_name("Sheet1")
row_count = ws.nrows
col_count = ws.ncols

def get_attendance(for_day):
    p_count = 0
    a_count = 0
    for i in range(col_count):
        if ws.cell_value(0, i) == for_day:
            for j in range(row_count - 1):
                if ws.cell_value(j + 1, i) == 1:
                    p_count = p_count + 1
                elif ws.cell_value(j + 1, i) == 0:
                    a_count = a_count + 1

    print("Number of people present: ", p_count)
    print("Number of people absent: ", a_count)


for_day = input("Enter the day to check the attendance: ").title()
get_attendance(for_day)
