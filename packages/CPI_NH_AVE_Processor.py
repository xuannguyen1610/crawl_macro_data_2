from CPI_Util import get_value_CPI_category

def cpi_categories_ave():
    range = "H11:H21"
    cpi_categories_ave = {}
    cpi_categories_ave["CPI_AVE_HADVAU"] = get_value_CPI_category(0,range)
    cpi_categories_ave["CPI_AVE_DUVTL"] = get_value_CPI_category(1,range)
    cpi_categories_ave["CPI_AVE_MMGDMN"] = get_value_CPI_category(2,range)
    cpi_categories_ave["CPI_AVE_NNVLXD"] = get_value_CPI_category(3,range)
    cpi_categories_ave["CPI_AVE_TBDDGD"] = get_value_CPI_category(4,range)
    cpi_categories_ave["CPI_AVE_TVDVYT"] = get_value_CPI_category(5,range)
    cpi_categories_ave["CPI_AVE_GT"] = get_value_CPI_category(6,range)
    cpi_categories_ave["CPI_AVE_BCVT"] = get_value_CPI_category(7,range)
    cpi_categories_ave["CPI_AVE_GD"] = get_value_CPI_category(8,range)
    cpi_categories_ave["CPI_AVE_VHGTDL"] = get_value_CPI_category(9,range)
    cpi_categories_ave["CPI_AVE_DDVDVK"] = get_value_CPI_category(10,range)

    return cpi_categories_ave



