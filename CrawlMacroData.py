from IIP_Processor import get_value_TT_IIP_TOAN_NGANH,get_value_TT_IIP_NGANH_CNCBCT
from GDP_Processor import get_value_TT_GDP
from Tongmuc_Processor import get_dictionary_TMBL
from FDI_Processor import get_value_TTLK_FDI_GN,get_value_FDI_GN,get_value_TTLK_FDI_DK,get_value_FDI_DK
from XNK_Processor import get_value_XNK_NK,get_value_XNK_XK
from CPI_NH_YOY_Processor import cpi_categories_yoy
from CPI_NH_AVE_Processor import cpi_categories_ave
from CPI_Processor import get_value_CPI_TT_MOM,get_value_CPI_TT_YOY,get_value_CPI_TT_AVE
from TMLTLP_Processor import get_value_TMBL_TTLTLP

print(f"TT_IIP_TOAN_NGANH: {get_value_TT_IIP_TOAN_NGANH()}")
print(f"TT_IIP_NGANH_CNCBCT:{get_value_TT_IIP_NGANH_CNCBCT()}")
print(f"TT_GDP:{get_value_TT_GDP()}")
print(f"TMBL:{get_dictionary_TMBL()}")
print(f"FDI_GN: {get_value_FDI_GN()}")
print(f"FDI_DK: {get_value_FDI_DK()}")
print(f"TTLK_FDI_GN: {get_value_TTLK_FDI_GN()}")
print(f"TTLK_FDI_DK: {get_value_TTLK_FDI_DK()}")
print(f"XNK_XK: {get_value_XNK_XK()}")
print(f"XNK_NK: {get_value_XNK_NK()}")
print(f"CPI_NH_YOY: {cpi_categories_yoy()}")
print(f"CPI_NH_AVE: {cpi_categories_ave()}")
print(f"CPI_TT_YOY: {get_value_CPI_TT_YOY()}")
print(f"CPI_TT_MOM: {get_value_CPI_TT_MOM()}")
print(f"CPI_TT_AVE: {get_value_CPI_TT_AVE()}")
print(f"TMBL_TTLTLP: {get_value_TMBL_TTLTLP()}")
