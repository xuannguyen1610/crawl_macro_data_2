from packages import IIP_Processor, GDP_Processor, Tongmuc_Processor, FDI_Processor, XNK_Processor, CPI_NH_YOY_Processor, CPI_NH_AVE_Processor, CPI_Processor, TMLTLP_Processor


print(f"TT_IIP_TOAN_NGANH: {IIP_Processor.get_value_TT_IIP_TOAN_NGANH()}")
print(f"TT_IIP_NGANH_CNCBCT:{IIP_Processor.get_value_TT_IIP_NGANH_CNCBCT()}")
print(f"TT_GDP:{GDP_Processor.get_value_TT_GDP()}")
print(f"TMBL:{Tongmuc_Processor.get_dictionary_TMBL()}")
print(f"FDI_GN: {FDI_Processor.get_value_FDI_GN()}")
print(f"FDI_DK: {FDI_Processor.get_value_FDI_DK()}")
print(f"TTLK_FDI_GN: {FDI_Processor.get_value_TTLK_FDI_GN()}")
print(f"TTLK_FDI_DK: {FDI_Processor.get_value_TTLK_FDI_DK()}")
print(f"XNK_XK: {XNK_Processor.get_value_XNK_XK()}")
print(f"XNK_NK: {XNK_Processor.get_value_XNK_NK()}")
print(f"CPI_NH_YOY: {CPI_NH_YOY_Processor.cpi_categories_yoy()}")
print(f"CPI_NH_AVE: {CPI_NH_AVE_Processor.cpi_categories_ave()}")
print(f"CPI_TT_YOY: {CPI_Processor.get_value_CPI_TT_YOY()}")
print(f"CPI_TT_MOM: {CPI_Processor.get_value_CPI_TT_MOM()}")
print(f"CPI_TT_AVE: {CPI_Processor.get_value_CPI_TT_AVE()}")
print(f"TMBL_TTLTLP: {TMLTLP_Processor.get_value_TMBL_TTLTLP()}")
