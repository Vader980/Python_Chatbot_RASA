import xlrd

directory = ('C://Users/ukmak/OneDrive/Desktop/NWU Documents/MODULES/Third Year/CMPG 313/Project/Project Files/AIPROJECTXLS.xls')
fileWorkbook = xlrd.open_workbook(directory)
sheet = fileWorkbook.sheet_by_index(0)

print(sheet.cell_value(1, 0))
