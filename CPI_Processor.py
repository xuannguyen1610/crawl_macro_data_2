from CPI_Util import get_value
from ValueConverter import convert_value_file_TCTK

header_CPI = "CHỈ SỐ GIÁ TIÊU DÙNG"


def get_value_CPI_TT_YOY():
    header = get_value("A9")
    if header == header_CPI:
         raw_CPI_TT_YOY = get_value("E9")
         CPI_TT_YOY = convert_value_file_TCTK(raw_CPI_TT_YOY)
         return CPI_TT_YOY
    else:
        return None


def get_value_CPI_TT_MOM():
    header = get_value("A9")
    if header == header_CPI:
         raw_CPI_TT_MOM = get_value("G9")
         CPI_TT_MOM = convert_value_file_TCTK(raw_CPI_TT_MOM)
         return CPI_TT_MOM
    else:
        return None


def get_value_CPI_TT_AVE():
    header = get_value("A9")
    if header == header_CPI:
         raw_CPI_TT_AVE = get_value("H9")
         CPI_TT_AVE = convert_value_file_TCTK(raw_CPI_TT_AVE)
         return CPI_TT_AVE
    else:
        return None