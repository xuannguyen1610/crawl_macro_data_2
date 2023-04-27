from processor import IIP, GDP, Tongmuc, FDI, XNK, CPI_NH_YOY, CPI_NH_AVE, CPI, TMLTLP
from MacroDataRepository import insert_data_to_database
from MacroDataModel import Macro_Data

date = '2023-03-31'

value_TT_IIP_TOAN_NGANH = IIP.get_value_TT_IIP_TOAN_NGANH()
value_TT_IIP_NGANH_CNCBCT = IIP.get_value_TT_IIP_NGANH_CNCBCT()
value_TT_GDP = GDP.get_value_TT_GDP()
value_TMBL = Tongmuc.get_dictionary_TMBL()
value_FDI_GN = FDI.get_value_FDI_GN()
value_FDI_DK = FDI.get_value_FDI_DK()
value_TTLK_FDI_GN = FDI.get_value_TTLK_FDI_GN()
value_TTLK_FDI_DK = FDI.get_value_TTLK_FDI_DK()
value_XNK_XK = XNK.get_value_XNK_XK()
value_XNK_NK = XNK.get_value_XNK_NK()
value_CPI_NH_YOY = CPI_NH_YOY.cpi_categories_yoy()
value_CPI_NH_AVE = CPI_NH_AVE.cpi_categories_ave()
value_CPI_TT_YOY = CPI.get_value_CPI_TT_YOY()
value_CPI_TT_MOM = CPI.get_value_CPI_TT_MOM()
value_CPI_TT_AVE = CPI.get_value_CPI_TT_AVE()
value_TMBL_TTLTLP = TMLTLP.get_value_TMBL_TTLTLP()

IS_DEBUG = False
if IS_DEBUG:

    print(f"TT_IIP_TOAN_NGANH: {value_TT_IIP_TOAN_NGANH}")
    print(f"TT_IIP_NGANH_CNCBCT:{value_TT_IIP_NGANH_CNCBCT}")
    print(f"TT_GDP:{value_TT_GDP}")
    print(f"TMBL:{value_TMBL}")
    print(f"FDI_GN: {value_FDI_GN}")
    print(f"FDI_DK: {value_FDI_DK}")
    print(f"TTLK_FDI_GN: {value_TTLK_FDI_GN}")
    print(f"TTLK_FDI_DK: {value_TTLK_FDI_DK}")
    print(f"XNK_XK: {value_XNK_XK}")
    print(f"XNK_NK: {value_XNK_NK}")
    print(f"CPI_NH_YOY: {value_CPI_NH_YOY}")
    print(f"CPI_NH_AVE: {value_CPI_NH_AVE}")
    print(f"CPI_TT_YOY: {value_CPI_TT_YOY}")
    print(f"CPI_TT_MOM: {value_CPI_TT_MOM}")
    print(f"CPI_TT_AVE: {value_CPI_TT_AVE}")
    print(f"TMBL_TTLTLP: {value_TMBL_TTLTLP}")

else:
    data_TT_IIP_TOAN_NGANH = Macro_Data('IIP',
                                        'TT_IIP_TOAN_NGANH',
                                        '',
                                        date,
                                        value_TT_IIP_TOAN_NGANH)
    data_TT_IIP_NGANH_CNCBCT = Macro_Data('IIP',
                                          'TT_IIP_NGANH_CNCBCT',
                                          '',
                                          date,
                                          value_TT_IIP_NGANH_CNCBCT)
    data_TMBL_TT = Macro_Data('TMBL',
                              'TMBL_TT',
                              '',
                              date,
                              value_TMBL['TMBL_TT'])
    data_TMBL_BLHH = Macro_Data('TMBL',
                                'TMBL_BLHH',
                                '',
                                date,
                                value_TMBL['TMBL_BLHH'])
    data_TMBL_DV = Macro_Data('TMBL',
                              'TMBL_DV',
                              '',
                              date,
                              value_TMBL['TMBL_DV'])
    data_TMBL_DLLH = Macro_Data('TMBL',
                                'TMBL_DLLH',
                                '',
                                date,
                                value_TMBL['TMBL_DLLH'])
    data_TMBL_TTLTLP = Macro_Data('TMBL',
                                  'TMBL_TTLTLP',
                                  '',
                                  date,
                                  value_TMBL_TTLTLP)
    data_TT_GDP = Macro_Data('GDP',
                             'TT_GDP',
                             '',
                             date,
                             value_TT_GDP)
    data_CPI_TT_MOM = Macro_Data('CPI',
                                 'CPI_TT_MOM',
                                 '',
                                 date,
                                 value_CPI_TT_MOM)
    data_CPI_TT_YOY = Macro_Data('CPI',
                                 'CPI_TT_YOY',
                                 '',
                                 date,
                                 value_CPI_TT_YOY)
    data_CPI_TT_AVE = Macro_Data('CPI',
                                 'CPI_TT_AVE',
                                 '',
                                 date,
                                 value_CPI_TT_AVE)
    data_FDI_GN = Macro_Data('FDI',
                             'FDI_GN',
                             '',
                             date,
                             value_FDI_GN)
    data_FDI_DK = Macro_Data('FDI',
                             'FDI_DK',
                             '',
                             date,
                             value_FDI_DK)
    data_TTLK_FDI_GN = Macro_Data('FDI',
                                  'TTLK_FDI_GN',
                                  '',
                                  date,
                                  value_TTLK_FDI_GN)
    data_TTLK_FDI_DK = Macro_Data('FDI',
                                  'TTLK_FDI_DK',
                                  '',
                                  date,
                                  value_TTLK_FDI_DK)
    data_XNK_XK = Macro_Data('XNK',
                             'XNK_XK',
                             '',
                             date,
                             value_XNK_XK)
    data_XNK_NK = Macro_Data('XNK',
                             'XNK_NK',
                             '',
                             date,
                             value_XNK_NK)

    data_CPI_YOY_HADVAU = Macro_Data('CC_CPI_NH',
                                     'CC_CPI_NH_YOY',
                                     'Hàng ăn và dịch vụ ăn uống',
                                     date,
                                     value_CPI_NH_YOY['CPI_YOY_HADVAU'])
    data_CPI_YOY_DUVTL = Macro_Data('CC_CPI_NH',
                                    'CC_CPI_NH_YOY',
                                    'Đồ uống và thuốc lá',
                                    date,
                                    value_CPI_NH_YOY['CPI_YOY_DUVTL'])
    data_CPI_YOY_MMGDMN = Macro_Data('CC_CPI_NH',
                                     'CC_CPI_NH_YOY',
                                     'May mặc, giày dép và mũ nón',
                                     date,
                                     value_CPI_NH_YOY['CPI_YOY_MMGDMN'])
    data_CPI_YOY_NNVLXD = Macro_Data('CC_CPI_NH',
                                     'CC_CPI_NH_YOY',
                                     'Nhà ở và vật liệu xây dựng',
                                     date,
                                     value_CPI_NH_YOY['CPI_YOY_NNVLXD'])
    data_CPI_YOY_TBDDGD = Macro_Data('CC_CPI_NH',
                                     'CC_CPI_NH_YOY',
                                     'Thiết bị và đồ dùng gia đình',
                                     date,
                                     value_CPI_NH_YOY['CPI_YOY_TBDDGD'])
    data_CPI_YOY_TVDVYT = Macro_Data('CC_CPI_NH',
                                     'CC_CPI_NH_YOY',
                                     'Thuốc và dịch vụ y tế',
                                     date,
                                     value_CPI_NH_YOY['CPI_YOY_TVDVYT'])
    data_CPI_YOY_GT = Macro_Data('CC_CPI_NH',
                                 'CC_CPI_NH_YOY',
                                 'Giao thông',
                                 date,
                                 value_CPI_NH_YOY['CPI_YOY_GT'])
    data_CPI_YOY_BCVT = Macro_Data('CC_CPI_NH',
                                   'CC_CPI_NH_YOY',
                                   'Bưu chính viễn thông',
                                   date,
                                   value_CPI_NH_YOY['CPI_YOY_BCVT'])
    data_CPI_YOY_GD = Macro_Data('CC_CPI_NH',
                                 'CC_CPI_NH_YOY',
                                 'Giáo dục',
                                 date,
                                 value_CPI_NH_YOY['CPI_YOY_GD'])
    data_CPI_YOY_VHGTDL = Macro_Data('CC_CPI_NH',
                                     'CC_CPI_NH_YOY',
                                     'Văn hóa giái trí và du lịch',
                                     date,
                                     value_CPI_NH_YOY['CPI_YOY_VHGTDL'])
    data_CPI_YOY_DDVDVK = Macro_Data('CC_CPI_NH',
                                     'CC_CPI_NH_YOY',
                                     'Đồ dùng và dịch vụ khác',
                                     date,
                                     value_CPI_NH_YOY['CPI_YOY_DDVDVK'])

    data_CPI_AVE_HADVAU = Macro_Data('CC_CPI_NH',
                                     'CC_CPI_NH_AVE',
                                     'Hàng ăn và dịch vụ ăn uống',
                                     date,
                                     value_CPI_NH_AVE['CPI_AVE_HADVAU'])
    data_CPI_AVE_DUVTL = Macro_Data('CC_CPI_NH',
                                    'CC_CPI_NH_AVE',
                                    'Đồ uống và thuốc lá',
                                    date,
                                    value_CPI_NH_AVE['CPI_AVE_DUVTL'])
    data_CPI_AVE_MMGDMN = Macro_Data('CC_CPI_NH',
                                     'CC_CPI_NH_AVE',
                                     'May mặc, giày dép và mũ nón',
                                     date,
                                     value_CPI_NH_AVE['CPI_AVE_MMGDMN'])
    data_CPI_AVE_NNVLXD = Macro_Data('CC_CPI_NH',
                                     'CC_CPI_NH_AVE',
                                     'Nhà ở và vật liệu xây dựng',
                                     date,
                                     value_CPI_NH_AVE['CPI_AVE_NNVLXD'])
    data_CPI_AVE_TBDDGD = Macro_Data('CC_CPI_NH',
                                     'CC_CPI_NH_AVE',
                                     'Thiết bị và đồ dùng gia đình',
                                     date,
                                     value_CPI_NH_AVE['CPI_AVE_TBDDGD'])
    data_CPI_AVE_TVDVYT = Macro_Data('CC_CPI_NH',
                                     'CC_CPI_NH_AVE',
                                     'Thuốc và dịch vụ y tế',
                                     date,
                                     value_CPI_NH_AVE['CPI_AVE_TVDVYT'])
    data_CPI_AVE_GT = Macro_Data('CC_CPI_NH',
                                 'CC_CPI_NH_AVE',
                                 'Giao thông',
                                 date,
                                 value_CPI_NH_AVE['CPI_AVE_GT'])
    data_CPI_AVE_BCVT = Macro_Data('CC_CPI_NH',
                                   'CC_CPI_NH_AVE',
                                   'Bưu chính viễn thông',
                                   date,
                                   value_CPI_NH_AVE['CPI_AVE_BCVT'])
    data_CPI_AVE_GD = Macro_Data('CC_CPI_NH',
                                 'CC_CPI_NH_AVE',
                                 'Giáo dục',
                                 date,
                                 value_CPI_NH_AVE['CPI_AVE_GD'])
    data_CPI_AVE_VHGTDL = Macro_Data('CC_CPI_NH',
                                     'CC_CPI_NH_AVE',
                                     'Văn hóa giái trí và du lịch',
                                     date,
                                     value_CPI_NH_AVE['CPI_AVE_VHGTDL'])
    data_CPI_AVE_DDVDVK = Macro_Data('CC_CPI_NH',
                                     'CC_CPI_NH_AVE',
                                     'Đồ dùng và dịch vụ khác',
                                     date,
                                     value_CPI_NH_AVE['CPI_AVE_DDVDVK'])

    list_data = [data_TT_IIP_TOAN_NGANH, data_TT_IIP_NGANH_CNCBCT, data_TMBL_TT, data_TMBL_BLHH, data_TMBL_DV,
                 data_TMBL_DLLH, data_TMBL_TTLTLP, data_TT_GDP, data_CPI_TT_MOM, data_CPI_TT_YOY, data_CPI_TT_AVE,
                 data_FDI_GN, data_FDI_DK, data_TTLK_FDI_GN, data_TTLK_FDI_DK, data_XNK_XK, data_XNK_NK,
                 data_CPI_YOY_HADVAU, data_CPI_YOY_DUVTL, data_CPI_YOY_MMGDMN, data_CPI_YOY_NNVLXD, data_CPI_YOY_TBDDGD,
                 data_CPI_YOY_TVDVYT, data_CPI_YOY_GT, data_CPI_YOY_BCVT, data_CPI_YOY_GD, data_CPI_YOY_VHGTDL,
                 data_CPI_YOY_DDVDVK, data_CPI_AVE_HADVAU, data_CPI_AVE_DUVTL, data_CPI_AVE_MMGDMN, data_CPI_AVE_NNVLXD,
                 data_CPI_AVE_TBDDGD, data_CPI_AVE_TVDVYT, data_CPI_AVE_GT, data_CPI_AVE_BCVT, data_CPI_AVE_GD,
                 data_CPI_AVE_VHGTDL, data_CPI_AVE_DDVDVK]

    for data in list_data:
        insert_data_to_database(data)