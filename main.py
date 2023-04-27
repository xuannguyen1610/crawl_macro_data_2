from MacroDataRepository import insert_data_to_database
from MacroDataService import list_data

for data in list_data:
    insert_data_to_database(data)