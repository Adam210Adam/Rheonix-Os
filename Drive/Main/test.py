from xlrd import open_workbook
from xlutils.copy import copy

xl_file = r'C:\Users\Adam\Desktop\adam folders\Rheonix OS\Drive\Main\DAR.xls'
rb = open_workbook(xl_file, formatting_info=True)
wb = copy(rb)
sheet = wb.get_sheet(0)
sheet.write(0,2,'New_Data_For_Cell')
wb.save(xl_file)