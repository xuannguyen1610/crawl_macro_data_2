import mysql.connector

mydb = mysql.connector.connect(
    host="157.230.244.233",
    user="stock_admin",
    password="aVBrVDczZzJ5OUVma3JR",
    database="stock"
)

def insert_data_to_database(data):
    cursor = mydb.cursor()
    params = (data.type, data.code, data.category, data.date, data.value)
    add_data_query = "INSERT INTO macro_data_test(type, code, category, date, value) VALUES(%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE value=VALUES(value)"

    cursor.execute(add_data_query,params)
    mydb.commit()

    cursor.close()