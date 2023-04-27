from CPI_Util import get_value_CPI_category

def cpi_categories_yoy():
    range = "E11:E21"
    cpi_categories_yoy = {}
    cpi_categories_yoy["CPI_YOY_HADVAU"] = get_value_CPI_category(0,range)
    cpi_categories_yoy["CPI_YOY_DUVTL"] = get_value_CPI_category(1,range)
    cpi_categories_yoy["CPI_YOY_MMGDMN"] = get_value_CPI_category(2,range)
    cpi_categories_yoy["CPI_YOY_NNVLXD"] = get_value_CPI_category(3,range)
    cpi_categories_yoy["CPI_YOY_TBDDGD"] = get_value_CPI_category(4,range)
    cpi_categories_yoy["CPI_YOY_TVDVYT"] = get_value_CPI_category(5,range)
    cpi_categories_yoy["CPI_YOY_GT"] = get_value_CPI_category(6,range)
    cpi_categories_yoy["CPI_YOY_BCVT"] = get_value_CPI_category(7,range)
    cpi_categories_yoy["CPI_YOY_GD"] = get_value_CPI_category(8,range)
    cpi_categories_yoy["CPI_YOY_VHGTDL"] = get_value_CPI_category(9,range)
    cpi_categories_yoy["CPI_YOY_DDVDVK"] = get_value_CPI_category(10,range)

    return cpi_categories_yoy

