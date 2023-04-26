from ExcelUtil import load_sheet_from_file, get_data_from_sheet
from ConvertValue import convert_value_file_TCTK

input_file = r"C:\Users\Admin\Downloads\Macro_data\02-Bieu-T3.2023-1.xlsx"
sheet_name = "1.GDP"
header_GDP = "TỔNG SỐ"

sheet = load_sheet_from_file(input_file,sheet_name)

def get_value(cell):
    return get_data_from_sheet(sheet,cell)


def get_value_TT_GDP():
    header = get_value("A8")
    if header == header_GDP:
         raw_TT_GDP = get_value("G8")
         TT_GDP = convert_value_file_TCTK(raw_TT_GDP)
         return TT_GDP
    else:
        return None
