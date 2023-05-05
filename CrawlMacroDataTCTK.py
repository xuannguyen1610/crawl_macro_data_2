from processor import IIP, Tongmuc, CPI_NH_YOY, CPI_NH_AVE, CPI
from MacroDataRepository import insert_data_to_database
from MacroDataModel import Macro_Data
import datetime


date = '2023-04-30'
date_object = datetime.datetime.strptime(date, "%Y-%m-%d")
year = date_object.year
month = date_object.month
quarter = 0

value_TT_IIP_TOAN_NGANH = IIP.get_value_TT_IIP_TOAN_NGANH()
value_TT_IIP_NGANH_CNCBCT = IIP.get_value_TT_IIP_NGANH_CNCBCT()
value_TMBL = Tongmuc.get_dictionary_TMBL()
value_CPI_NH_YOY = CPI_NH_YOY.cpi_categories_yoy()
value_CPI_NH_AVE = CPI_NH_AVE.cpi_categories_ave()
value_CPI_TT_YOY = CPI.get_value_CPI_TT_YOY()
value_CPI_TT_MOM = CPI.get_value_CPI_TT_MOM()
value_CPI_TT_AVE = CPI.get_value_CPI_TT_AVE()


IS_DEBUG = True
if IS_DEBUG:

    print(f"TT_IIP_TOAN_NGANH: {value_TT_IIP_TOAN_NGANH}")
    print(f"TT_IIP_NGANH_CNCBCT:{value_TT_IIP_NGANH_CNCBCT}")
    print(f"TMBL:{value_TMBL}")
    print(f"CPI_NH_YOY: {value_CPI_NH_YOY}")
    print(f"CPI_NH_AVE: {value_CPI_NH_AVE}")
    print(f"CPI_TT_YOY: {value_CPI_TT_YOY}")
    print(f"CPI_TT_MOM: {value_CPI_TT_MOM}")
    print(f"CPI_TT_AVE: {value_CPI_TT_AVE}")

else:
    data_TT_IIP_TOAN_NGANH = Macro_Data('IIP',
                                        'TT_IIP_TOAN_NGANH',
                                        '',
                                        date,
                                        year,
                                        month,
                                        value_TT_IIP_TOAN_NGANH,
                                        quarter)
    data_TT_IIP_NGANH_CNCBCT = Macro_Data('IIP',
                                          'TT_IIP_NGANH_CNCBCT',
                                          '',
                                          date,
                                          year,
                                          month,
                                          value_TT_IIP_NGANH_CNCBCT,
                                          quarter)
    data_TMBL_TT = Macro_Data('TMBL',
                              'TMBL_TT',
                              '',
                              date,
                              year,
                              month,
                              value_TMBL['TMBL_TT'],
                              quarter)
    data_TMBL_BLHH = Macro_Data('TMBL',
                                'TMBL_BLHH',
                                '',
                                date,
                                year,
                                month,
                                value_TMBL['TMBL_BLHH'],
                                quarter)
    data_TMBL_DV = Macro_Data('TMBL',
                              'TMBL_DV',
                              '',
                              date,
                              year,
                              month,
                              value_TMBL['TMBL_DV'],
                              quarter)
    data_TMBL_DLLH = Macro_Data('TMBL',
                                'TMBL_DLLH',
                                '',
                                date,
                                year,
                                month,
                                value_TMBL['TMBL_DLLH'],
                                quarter)
    data_CPI_TT_MOM = Macro_Data('CPI_TT',
                                 'CPI_TT_MOM',
                                 '',
                                 date,
                                 year,
                                 month,
                                 value_CPI_TT_MOM,
                                 quarter)
    data_CPI_TT_YOY = Macro_Data('CPI_TT',
                                 'CPI_TT_YOY',
                                 '',
                                 date,
                                 year,
                                 month,
                                 value_CPI_TT_YOY,
                                 quarter)
    data_CPI_TT_AVE = Macro_Data('CPI_TT',
                                 'CPI_TT_AVE',
                                 '',
                                 date,
                                 year,
                                 month,
                                 value_CPI_TT_AVE,
                                 quarter)

    data_CPI_YOY_HADVAU = Macro_Data('CC_CPI_NH',
                                     'CC_CPI_NH_YOY',
                                     'Hàng ăn và dịch vụ ăn uống',
                                     date,
                                     year,
                                     month,
                                     value_CPI_NH_YOY['CPI_YOY_HADVAU'],
                                     quarter)
    data_CPI_YOY_DUVTL = Macro_Data('CC_CPI_NH',
                                    'CC_CPI_NH_YOY',
                                    'Đồ uống và thuốc lá',
                                    date,
                                    year,
                                    month,
                                    value_CPI_NH_YOY['CPI_YOY_DUVTL'],
                                    quarter)
    data_CPI_YOY_MMGDMN = Macro_Data('CC_CPI_NH',
                                     'CC_CPI_NH_YOY',
                                     'May mặc, giày dép và mũ nón',
                                     date,
                                     year,
                                     month,
                                     value_CPI_NH_YOY['CPI_YOY_MMGDMN'],
                                     quarter)
    data_CPI_YOY_NNVLXD = Macro_Data('CC_CPI_NH',
                                     'CC_CPI_NH_YOY',
                                     'Nhà ở và vật liệu xây dựng',
                                     date,
                                     year,
                                     month,
                                     value_CPI_NH_YOY['CPI_YOY_NNVLXD'],
                                     quarter)
    data_CPI_YOY_TBDDGD = Macro_Data('CC_CPI_NH',
                                     'CC_CPI_NH_YOY',
                                     'Thiết bị và đồ dùng gia đình',
                                     date,
                                     year,
                                     month,
                                     value_CPI_NH_YOY['CPI_YOY_TBDDGD'],
                                     quarter)
    data_CPI_YOY_TVDVYT = Macro_Data('CC_CPI_NH',
                                     'CC_CPI_NH_YOY',
                                     'Thuốc và dịch vụ y tế',
                                     date,
                                     year,
                                     month,
                                     value_CPI_NH_YOY['CPI_YOY_TVDVYT'],
                                     quarter)
    data_CPI_YOY_GT = Macro_Data('CC_CPI_NH',
                                 'CC_CPI_NH_YOY',
                                 'Giao thông',
                                 date,
                                 year,
                                 month,
                                 value_CPI_NH_YOY['CPI_YOY_GT'],
                                 quarter)
    data_CPI_YOY_BCVT = Macro_Data('CC_CPI_NH',
                                   'CC_CPI_NH_YOY',
                                   'Bưu chính viễn thông',
                                   date,
                                   year,
                                   month,
                                   value_CPI_NH_YOY['CPI_YOY_BCVT'],
                                   quarter)
    data_CPI_YOY_GD = Macro_Data('CC_CPI_NH',
                                 'CC_CPI_NH_YOY',
                                 'Giáo dục',
                                 date,
                                 year,
                                 month,
                                 value_CPI_NH_YOY['CPI_YOY_GD'],
                                 quarter)
    data_CPI_YOY_VHGTDL = Macro_Data('CC_CPI_NH',
                                     'CC_CPI_NH_YOY',
                                     'Văn hóa giái trí và du lịch',
                                     date,
                                     year,
                                     month,
                                     value_CPI_NH_YOY['CPI_YOY_VHGTDL'],
                                     quarter)
    data_CPI_YOY_DDVDVK = Macro_Data('CC_CPI_NH',
                                     'CC_CPI_NH_YOY',
                                     'Đồ dùng và dịch vụ khác',
                                     date,
                                     year,
                                     month,
                                     value_CPI_NH_YOY['CPI_YOY_DDVDVK'],
                                     quarter)

    data_CPI_AVE_HADVAU = Macro_Data('CC_CPI_NH',
                                     'CC_CPI_NH_AVE',
                                     'Hàng ăn và dịch vụ ăn uống',
                                     date,
                                     year,
                                     month,
                                     value_CPI_NH_AVE['CPI_AVE_HADVAU'],
                                     quarter)
    data_CPI_AVE_DUVTL = Macro_Data('CC_CPI_NH',
                                    'CC_CPI_NH_AVE',
                                    'Đồ uống và thuốc lá',
                                    date,
                                    year,
                                    month,
                                    value_CPI_NH_AVE['CPI_AVE_DUVTL'],
                                    quarter)
    data_CPI_AVE_MMGDMN = Macro_Data('CC_CPI_NH',
                                     'CC_CPI_NH_AVE',
                                     'May mặc, giày dép và mũ nón',
                                     date,
                                     year,
                                     month,
                                     value_CPI_NH_AVE['CPI_AVE_MMGDMN'],
                                     quarter)
    data_CPI_AVE_NNVLXD = Macro_Data('CC_CPI_NH',
                                     'CC_CPI_NH_AVE',
                                     'Nhà ở và vật liệu xây dựng',
                                     date,
                                     year,
                                     month,
                                     value_CPI_NH_AVE['CPI_AVE_NNVLXD'],
                                     quarter)
    data_CPI_AVE_TBDDGD = Macro_Data('CC_CPI_NH',
                                     'CC_CPI_NH_AVE',
                                     'Thiết bị và đồ dùng gia đình',
                                     date,
                                     year,
                                     month,
                                     value_CPI_NH_AVE['CPI_AVE_TBDDGD'],
                                     quarter)
    data_CPI_AVE_TVDVYT = Macro_Data('CC_CPI_NH',
                                     'CC_CPI_NH_AVE',
                                     'Thuốc và dịch vụ y tế',
                                     date,
                                     year,
                                     month,
                                     value_CPI_NH_AVE['CPI_AVE_TVDVYT'],
                                     quarter)
    data_CPI_AVE_GT = Macro_Data('CC_CPI_NH',
                                 'CC_CPI_NH_AVE',
                                 'Giao thông',
                                 date,
                                 year,
                                 month,
                                 value_CPI_NH_AVE['CPI_AVE_GT'],
                                 quarter)
    data_CPI_AVE_BCVT = Macro_Data('CC_CPI_NH',
                                   'CC_CPI_NH_AVE',
                                   'Bưu chính viễn thông',
                                   date,
                                   year,
                                   month,
                                   value_CPI_NH_AVE['CPI_AVE_BCVT'],
                                   quarter)
    data_CPI_AVE_GD = Macro_Data('CC_CPI_NH',
                                 'CC_CPI_NH_AVE',
                                 'Giáo dục',
                                 date,
                                 year,
                                 month,
                                 value_CPI_NH_AVE['CPI_AVE_GD'],
                                 quarter)
    data_CPI_AVE_VHGTDL = Macro_Data('CC_CPI_NH',
                                     'CC_CPI_NH_AVE',
                                     'Văn hóa giái trí và du lịch',
                                     date,
                                     year,
                                     month,
                                     value_CPI_NH_AVE['CPI_AVE_VHGTDL'],
                                     quarter)
    data_CPI_AVE_DDVDVK = Macro_Data('CC_CPI_NH',
                                     'CC_CPI_NH_AVE',
                                     'Đồ dùng và dịch vụ khác',
                                     date,
                                     year,
                                     month,
                                     value_CPI_NH_AVE['CPI_AVE_DDVDVK'],
                                     quarter)

    list_data = [data_TT_IIP_TOAN_NGANH, data_TT_IIP_NGANH_CNCBCT, data_TMBL_TT, data_TMBL_BLHH, data_TMBL_DV,
                 data_TMBL_DLLH, data_CPI_TT_MOM, data_CPI_TT_YOY, data_CPI_TT_AVE,
                 data_CPI_YOY_HADVAU, data_CPI_YOY_DUVTL, data_CPI_YOY_MMGDMN, data_CPI_YOY_NNVLXD, data_CPI_YOY_TBDDGD,
                 data_CPI_YOY_TVDVYT, data_CPI_YOY_GT, data_CPI_YOY_BCVT, data_CPI_YOY_GD, data_CPI_YOY_VHGTDL,
                 data_CPI_YOY_DDVDVK, data_CPI_AVE_HADVAU, data_CPI_AVE_DUVTL, data_CPI_AVE_MMGDMN, data_CPI_AVE_NNVLXD,
                 data_CPI_AVE_TBDDGD, data_CPI_AVE_TVDVYT, data_CPI_AVE_GT, data_CPI_AVE_BCVT, data_CPI_AVE_GD,
                 data_CPI_AVE_VHGTDL, data_CPI_AVE_DDVDVK]

    for data in list_data:
        insert_data_to_database(data)