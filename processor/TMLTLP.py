from ExcelUtil import load_sheet_from_file, get_data_from_sheet

input_file = r"C:\Users\Admin\Downloads\Macro_data\t3_2023.xlsx"
sheet_name = "Chỉ số tiêu dùng"
header_TTLTLP = "Tăng trưởng loại trừ lạm phát"


sheet = load_sheet_from_file(input_file,sheet_name)

def get_value(cell):
    return get_data_from_sheet(sheet,cell)


def get_value_TMBL_TTLTLP():
    header = get_value("B47")
    if header == header_TTLTLP:
         TMBL_TTLTLP = get_value("C47")
         return TMBL_TTLTLP
    else:
        return None
