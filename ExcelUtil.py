import openpyxl


def load_sheet_from_file(input_file, sheet_name):
    wb = openpyxl.load_workbook(input_file)
    sheet = wb[sheet_name]
    return sheet


def get_data_from_sheet(sheet,cell):
    return sheet[cell].value


def get_range_from_sheet(sheet,range):
    results = []
    range_value = sheet[range]
    for row in range_value:
        for cell in row:
            results.append(cell.value)
    return results