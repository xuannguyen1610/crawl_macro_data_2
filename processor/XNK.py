from ExcelUtil import load_sheet_from_file, get_data_from_sheet

input_file = r"C:\Users\Admin\Downloads\Macro_data\T3_2023\t3_2023.xlsx"
sheet_name = "Chỉ số thương mại"
header_XK = "Giá trị xuất khẩu"
header_NK = "Giá trị nhập khẩu"


sheet = load_sheet_from_file(input_file,sheet_name)

def get_value(cell):
    return get_data_from_sheet(sheet,cell)


def get_value_XNK_XK():
    header = get_value("B12")
    if header == header_XK:
         XNK_XK = round(get_value("C12"),2)
         return XNK_XK
    else:
        return None

def get_value_XNK_NK():
    header = get_value("B13")
    if header == header_NK:
         XNK_NK = round(get_value("C13"),2)
         return XNK_NK
    else:
        return None