from IIP_Processor import get_value_TT_IIP_TOAN_NGANH,get_value_TT_IIP_NGANH_CNCBCT
from GDP_Processor import get_value_TT_GDP
from Tongmuc_Processor import get_value_TMBL
from FDI_Processor import get_value_TTLK_FDI_GN,get_value_FDI_GN,get_value_TTLK_FDI_DK,get_value_FDI_DK
from XNK_Processor import get_value_XNK_NK,get_value_XNK_XK
from CPI_NH_YOY_Processor import cpi_categories_yoy
from CPI_Processor import get_value_CPI_TT_MOM,get_value_CPI_TT_YOY,get_value_CPI_TT_AVE
from TMLTLP_Processor import get_value_TMBL_TTLTLP

#print(get_value_TT_IIP_TOAN_NGANH())
#print(get_value_TT_IIP_NGANH_CNCBCT())
#print(get_value_TT_GDP())
#print(get_value_TMBL())
#print(get_value_TMBL_DV())
#print(f"TTLK_FDI_GN: {get_value_TTLK_FDI_GN()}")
#print(f"XNK_XK: {get_value_XNK_XK()}")
#print(f"CPI_DUVTL: {cpi_categories_yoy()['CPI_YOY_HADVAU']}")
#print(f"CPI_TT_MOM: {get_value_CPI_TT_YOY()}")
print(f"TMBL_TTLTLP: {get_value_TMBL_TTLTLP()}")
