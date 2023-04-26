from ExcelUtil import load_sheet_from_file, get_data_from_sheet
from ConvertValue import convert_value_file_TCTK

input_file = r"C:\Users\Admin\Downloads\Macro_data\02-Bieu-T3.2023-1.xlsx"
sheet_name = "7.IIP"
header_TN = "Toàn ngành công nghiệp"
header_CNCBCT = "Công nghiệp chế biến, chế tạo"

sheet = load_sheet_from_file(input_file,sheet_name)

def get_value(cell):
    return get_data_from_sheet(sheet,cell)


def get_value_TT_IIP_TOAN_NGANH():
    header = get_value("A10")
    if header == header_TN:
         raw_TT_IIP_TN = get_value("D10")
         TT_IIP_TOAN_NGANH = convert_value_file_TCTK(raw_TT_IIP_TN)
         return TT_IIP_TOAN_NGANH
    else:
        return None


def get_value_TT_IIP_NGANH_CNCBCT():
    if get_value("A17") == header_CNCBCT:
        raw_TT_IIP_CNCBCT = get_value("D17")
        TT_IIP_NGANH_CNCBCT = convert_value_file_TCTK(raw_TT_IIP_CNCBCT)
        return TT_IIP_NGANH_CNCBCT
    else:
        return None





