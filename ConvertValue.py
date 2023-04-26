def convert_value_file_TCTK(value:float):
    return round(value - 100,2)


def convert_value_file_SSI(value:float):
    return round(value*100,2)


def calculate_cpi_category(CPI_category,CPI_weight):
    return round(CPI_category*CPI_weight/100,2)