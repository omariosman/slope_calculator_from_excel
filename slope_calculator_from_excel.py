import xlrd

path = "file1.xlsx"

inputWorkbook = xlrd.open_workbook(path)

inputWorksheet = inputWorkbook.sheet_by_index(0)

print(inputWorksheet.nrows)
print(inputWorksheet.cell_value(0,1))
x1_list = []
x2_list = []
y1_list = []
y2_list = []
for i in range(inputWorksheet.nrows - 1):
    col = 0
    x1 = inputWorksheet.cell_value(i+1,col)
    x1_list.append(x1)
    col = col + 1;
    x2 = inputWorksheet.cell_value(i+1,col)
    x2_list.append(x2)
    col+=1;
    y1 = inputWorksheet.cell_value(i+1,col)
    y1_list.append(y1)
    col+=1
    y2 = inputWorksheet.cell_value(i+1,col)
    y2_list.append(y2)

print(x1_list)
print(x2_list)
print(y1_list)
print(y2_list)
    
all_slopes = []
for i in range(len(x1_list)):
    delta_x = x2_list[i] - x1_list[i]
    delta_y = y2_list[i] - y1_list[i]
    slope = (delta_y) / (delta_x)
    all_slopes.append(slope)
    
print(all_slopes)