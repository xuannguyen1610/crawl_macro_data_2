from ExcelUtil import load_sheet_from_file, get_data_from_sheet
from ConvertValue import convert_value_file_SSI

input_file = r"C:\Users\Admin\Downloads\Macro_data\t3_2023.xlsx"
sheet_name = "Chỉ số đầu tư"
header_FDI_GN = "Vốn FDI giải ngân trong tháng"
header_FDI_DK = "Vốn FDI đăng ký trong tháng"
header_FDI_LK = "Tăng trưởng YoY (lũy kế)"

sheet = load_sheet_from_file(input_file,sheet_name)

def get_value(cell):
    return get_data_from_sheet(sheet,cell)


def get_value_FDI_GN():
    header = get_value("B12")
    if header == header_FDI_GN:
         FDI_GN = get_value("C12")
         return FDI_GN
    else:
        return None


def get_value_FDI_DK():
    header = get_value("B28")
    if header == header_FDI_DK:
         FDI_DK = get_value("C28")
         return FDI_DK
    else:
        return None


def get_value_TTLK_FDI_GN():
    header = get_value("B14")
    if header == header_FDI_LK:
         raw_TTLK_FDI_GN = get_value("C14")
         TTLK_FDI_GN = convert_value_file_SSI(raw_TTLK_FDI_GN)
         return TTLK_FDI_GN
    else:
        return None


def get_value_TTLK_FDI_DK():
    header = get_value("B30")
    if header == header_FDI_LK:
         raw_TTLK_FDI_DK = get_value("C30")
         TTLK_FDI_DK = convert_value_file_SSI(raw_TTLK_FDI_DK)
         return TTLK_FDI_DK
    else:
        return None
