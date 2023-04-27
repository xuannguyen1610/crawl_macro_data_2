from packages import IIP_Processor, GDP_Processor, Tongmuc_Processor, FDI_Processor, XNK_Processor, CPI_NH_YOY_Processor, CPI_NH_AVE_Processor, CPI_Processor, TMLTLP_Processor
from MacroDataModel import Data

date = '2023-03-31'

data_TT_IIP_TOAN_NGANH = Data('IIP',
                              'TT_IIP_TOAN_NGANH',
                              '',
                              date,
                              IIP_Processor.get_value_TT_IIP_TOAN_NGANH())
data_TT_IIP_NGANH_CNCBCT = Data('IIP',
                                'TT_IIP_NGANH_CNCBCT',
                                '',
                                date,
                                IIP_Processor.get_value_TT_IIP_NGANH_CNCBCT())
data_TMBL_TT = Data('TMBL',
                    'TMBL_TT',
                    '',
                    date,
                    Tongmuc_Processor.get_dictionary_TMBL()['TMBL_TT'])
data_TMBL_BLHH = Data('TMBL',
                      'TMBL_BLHH',
                      '',
                      date,
                      Tongmuc_Processor.get_dictionary_TMBL()['TMBL_BLHH'])
data_TMBL_DV = Data('TMBL',
                    'TMBL_DV',
                    '',
                    date,
                    Tongmuc_Processor.get_dictionary_TMBL()['TMBL_DV'])
data_TMBL_DLLH = Data('TMBL',
                      'TMBL_DLLH',
                      '',
                      date,
                      Tongmuc_Processor.get_dictionary_TMBL()['TMBL_DLLH'])
data_TMBL_TTLTLP = Data('TMBL',
                        'TMBL_TTLTLP',
                        '',
                        date,
                        TMLTLP_Processor.get_value_TMBL_TTLTLP())
data_TT_GDP = Data('GDP',
                   'TT_GDP',
                   '',
                   date,
                   GDP_Processor.get_value_TT_GDP())
data_CPI_TT_MOM = Data('CPI',
                       'CPI_TT_MOM',
                       '',
                       date,
                       CPI_Processor.get_value_CPI_TT_MOM())
data_CPI_TT_YOY = Data('CPI',
                       'CPI_TT_YOY',
                       '',
                       date,
                       CPI_Processor.get_value_CPI_TT_YOY())
data_CPI_TT_AVE = Data('CPI',
                       'CPI_TT_AVE',
                       '',
                       date,
                       CPI_Processor.get_value_CPI_TT_AVE())
data_FDI_GN = Data('FDI',
                   'FDI_GN',
                   '',
                   date,
                   FDI_Processor.get_value_FDI_GN())
data_FDI_DK = Data('FDI',
                   'FDI_DK',
                   '',
                   date,
                   FDI_Processor.get_value_FDI_DK())
data_TTLK_FDI_GN = Data('FDI',
                        'TTLK_FDI_GN',
                        '',
                        date,
                        FDI_Processor.get_value_TTLK_FDI_GN())
data_TTLK_FDI_DK = Data('FDI',
                        'TTLK_FDI_DK',
                        '',
                        date,
                        FDI_Processor.get_value_TTLK_FDI_DK())
data_XNK_XK = Data('XNK',
                   'XNK_XK',
                   '',
                   date,
                   XNK_Processor.get_value_XNK_XK())
data_XNK_NK = Data('XNK',
                   'XNK_NK',
                   '',
                   date,
                   XNK_Processor.get_value_XNK_NK())


data_CPI_YOY_HADVAU = Data('CC_CPI_NH',
                           'CC_CPI_NH_YOY',
                           'Hàng ăn và dịch vụ ăn uống',
                           date,
                           CPI_NH_YOY_Processor.cpi_categories_yoy()['CPI_YOY_HADVAU'])
data_CPI_YOY_DUVTL = Data('CC_CPI_NH',
                          'CC_CPI_NH_YOY',
                          'Đồ uống và thuốc lá',
                          date,
                          CPI_NH_YOY_Processor.cpi_categories_yoy()['CPI_YOY_DUVTL'])
data_CPI_YOY_MMGDMN = Data('CC_CPI_NH',
                           'CC_CPI_NH_YOY',
                           'May mặc, giày dép và mũ nón',
                           date,
                           CPI_NH_YOY_Processor.cpi_categories_yoy()['CPI_YOY_MMGDMN'])
data_CPI_YOY_NNVLXD = Data('CC_CPI_NH',
                           'CC_CPI_NH_YOY',
                           'Nhà ở và vật liệu xây dựng',
                           date,
                           CPI_NH_YOY_Processor.cpi_categories_yoy()['CPI_YOY_NNVLXD'])
data_CPI_YOY_TBDDGD = Data('CC_CPI_NH',
                           'CC_CPI_NH_YOY',
                           'Thiết bị và đồ dùng gia đình',
                           date,
                           CPI_NH_YOY_Processor.cpi_categories_yoy()['CPI_YOY_TBDDGD'])
data_CPI_YOY_TVDVYT = Data('CC_CPI_NH',
                           'CC_CPI_NH_YOY',
                           'Thuốc và dịch vụ y tế',
                           date,
                           CPI_NH_YOY_Processor.cpi_categories_yoy()['CPI_YOY_TVDVYT'])
data_CPI_YOY_GT = Data('CC_CPI_NH',
                       'CC_CPI_NH_YOY',
                       'Giao thông',
                       date,
                       CPI_NH_YOY_Processor.cpi_categories_yoy()['CPI_YOY_GT'])
data_CPI_YOY_BCVT = Data('CC_CPI_NH',
                         'CC_CPI_NH_YOY',
                         'Bưu chính viễn thông',
                         date,
                         CPI_NH_YOY_Processor.cpi_categories_yoy()['CPI_YOY_BCVT'])
data_CPI_YOY_GD = Data('CC_CPI_NH',
                       'CC_CPI_NH_YOY',
                       'Giáo dục',
                       date,
                       CPI_NH_YOY_Processor.cpi_categories_yoy()['CPI_YOY_GD'])
data_CPI_YOY_VHGTDL = Data('CC_CPI_NH',
                           'CC_CPI_NH_YOY',
                           'Văn hóa giái trí và du lịch',
                           date,
                           CPI_NH_YOY_Processor.cpi_categories_yoy()['CPI_YOY_VHGTDL'])
data_CPI_YOY_DDVDVK = Data('CC_CPI_NH',
                           'CC_CPI_NH_YOY',
                           'Đồ dùng và dịch vụ khác',
                           date,
                           CPI_NH_YOY_Processor.cpi_categories_yoy()['CPI_YOY_DDVDVK'])



data_CPI_AVE_HADVAU = Data('CC_CPI_NH',
                           'CC_CPI_NH_AVE',
                           'Hàng ăn và dịch vụ ăn uống',
                           date,
                           CPI_NH_AVE_Processor.cpi_categories_ave()['CPI_AVE_HADVAU'])
data_CPI_AVE_DUVTL = Data('CC_CPI_NH',
                          'CC_CPI_NH_AVE',
                          'Đồ uống và thuốc lá',
                          date,
                          CPI_NH_AVE_Processor.cpi_categories_ave()['CPI_AVE_DUVTL'])
data_CPI_AVE_MMGDMN = Data('CC_CPI_NH',
                           'CC_CPI_NH_AVE',
                           'May mặc, giày dép và mũ nón',
                           date,
                           CPI_NH_AVE_Processor.cpi_categories_ave()['CPI_AVE_MMGDMN'])
data_CPI_AVE_NNVLXD = Data('CC_CPI_NH',
                           'CC_CPI_NH_AVE',
                           'Nhà ở và vật liệu xây dựng',
                           date,
                           CPI_NH_AVE_Processor.cpi_categories_ave()['CPI_AVE_NNVLXD'])
data_CPI_AVE_TBDDGD = Data('CC_CPI_NH',
                           'CC_CPI_NH_AVE',
                           'Thiết bị và đồ dùng gia đình',
                           date,
                           CPI_NH_AVE_Processor.cpi_categories_ave()['CPI_AVE_TBDDGD'])
data_CPI_AVE_TVDVYT = Data('CC_CPI_NH',
                           'CC_CPI_NH_AVE',
                           'Thuốc và dịch vụ y tế',
                           date,
                           CPI_NH_AVE_Processor.cpi_categories_ave()['CPI_AVE_TVDVYT'])
data_CPI_AVE_GT = Data('CC_CPI_NH',
                       'CC_CPI_NH_AVE',
                       'Giao thông',
                       date,
                       CPI_NH_AVE_Processor.cpi_categories_ave()['CPI_AVE_GT'])
data_CPI_AVE_BCVT = Data('CC_CPI_NH',
                         'CC_CPI_NH_AVE',
                         'Bưu chính viễn thông',
                         date,
                         CPI_NH_AVE_Processor.cpi_categories_ave()['CPI_AVE_BCVT'])
data_CPI_AVE_GD = Data('CC_CPI_NH',
                       'CC_CPI_NH_AVE',
                       'Giáo dục',
                       date,
                       CPI_NH_AVE_Processor.cpi_categories_ave()['CPI_AVE_GD'])
data_CPI_AVE_VHGTDL = Data('CC_CPI_NH',
                           'CC_CPI_NH_AVE',
                           'Văn hóa giái trí và du lịch',
                           date,
                           CPI_NH_AVE_Processor.cpi_categories_ave()['CPI_AVE_VHGTDL'])
data_CPI_AVE_DDVDVK = Data('CC_CPI_NH',
                           'CC_CPI_NH_AVE',
                           'Đồ dùng và dịch vụ khác',
                           date,
                           CPI_NH_AVE_Processor.cpi_categories_ave()['CPI_AVE_DDVDVK'])


list_data = [data_TT_IIP_TOAN_NGANH,data_TT_IIP_NGANH_CNCBCT,data_TMBL_TT,data_TMBL_BLHH,data_TMBL_DV,
             data_TMBL_DLLH,data_TMBL_TTLTLP,data_TT_GDP,data_CPI_TT_MOM,data_CPI_TT_YOY,data_CPI_TT_AVE,
             data_FDI_GN,data_FDI_DK,data_TTLK_FDI_GN,data_TTLK_FDI_DK,data_XNK_XK,data_XNK_NK,
             data_CPI_YOY_HADVAU,data_CPI_YOY_DUVTL,data_CPI_YOY_MMGDMN,data_CPI_YOY_NNVLXD,data_CPI_YOY_TBDDGD,
             data_CPI_YOY_TVDVYT,data_CPI_YOY_GT,data_CPI_YOY_BCVT,data_CPI_YOY_GD,data_CPI_YOY_VHGTDL,
             data_CPI_YOY_DDVDVK,data_CPI_AVE_HADVAU,data_CPI_AVE_DUVTL,data_CPI_AVE_MMGDMN,data_CPI_AVE_NNVLXD,
             data_CPI_AVE_TBDDGD,data_CPI_AVE_TVDVYT,data_CPI_AVE_GT,data_CPI_AVE_BCVT,data_CPI_AVE_GD,
             data_CPI_AVE_VHGTDL,data_CPI_AVE_DDVDVK]