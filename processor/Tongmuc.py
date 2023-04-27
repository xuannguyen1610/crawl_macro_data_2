from ExcelUtil import load_sheet_from_file, get_data_from_sheet, get_range_from_sheet
from ValueConverter import convert_value_file_TCTK

input_file = r"C:\Users\Admin\Downloads\Macro_data\02-Bieu-T3.2023-1.xlsx"
sheet_name = "20. Tongmuc"
header_TM = "TỔNG SỐ"

sheet = load_sheet_from_file(input_file,sheet_name)


def get_range_value():
    header = get_data_from_sheet(sheet,"A12")
    if header == header_TM:
        return get_range_from_sheet(sheet,"F12:F15")
    else:
        return None

range = get_range_value()

def get_value_TMBL(index):
    raw_value = range[index]
    value = convert_value_file_TCTK(raw_value)
    return value


def get_dictionary_TMBL():
    TMBL = {}
    TMBL["TMBL_TT"] = get_value_TMBL(0)
    TMBL["TMBL_BLHH"] = get_value_TMBL(1)
    TMBL["TMBL_DV"] = get_value_TMBL(2)
    TMBL["TMBL_DLLH"] = get_value_TMBL(3)
    return TMBL