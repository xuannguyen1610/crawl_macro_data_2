import mysql.connector

mydb = mysql.connector.connect(
    host="",
    user="",
    password="",
    database=""
)


def insert_data_to_database(data):
    cursor = mydb.cursor()
    params = (data.type, data.code,data.category, data.date,data.year, data.month, data.value, data.quarter)
    add_data_query = "INSERT INTO macro_data(type, code, category, date, year, month, value, quarter) VALUES(%s,%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE value=VALUES(value), date=VALUES(date)"

    cursor.execute(add_data_query,params)
    mydb.commit()

    cursor.close()
