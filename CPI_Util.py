from ExcelUtil import load_sheet_from_file, get_data_from_sheet, get_range_from_sheet
from ConvertValue import convert_value_file_TCTK, calculate_cpi_category

input_file = r"C:\Users\Admin\Downloads\Macro_data\02-Bieu-T3.2023-1.xlsx"
sheet_name = "24.CPI"
header_CPI = "CHỈ SỐ GIÁ TIÊU DÙNG"

CPI_weight = [33.56,2.73,5.7,18.82,6.74,5.39,9.67,3.14,6.17,4.55,3.53]
sheet = load_sheet_from_file(input_file,sheet_name)

def get_value(cell):
    return get_data_from_sheet(sheet,cell)


def get_range_value(range):
    header = get_data_from_sheet(sheet,"A9")
    if header == header_CPI:
        return get_range_from_sheet(sheet,range)
    else:
        return None


def get_value_CPI_category(index,range):
    range_value = get_range_value(range)
    raw_value = convert_value_file_TCTK(range_value[index])
    CPI_weight_category = CPI_weight[index]
    CPI_category = calculate_cpi_category(raw_value,CPI_weight_category)
    return CPI_category