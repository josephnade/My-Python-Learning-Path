import mysql.connector


def insertProduct(sql_attributes, values):
    connection = mysql.connector.connect(host="localhost", user="root", password="1234", database="node-app")
    cursor = connection.cursor()
    sql_query = f"INSERT INTO new_table({sql_attributes}) VALUES (%s,%s,%s,%s)"
    cursor.execute(sql_query, values)
    try:
        connection.commit()
        print(f"{cursor.rowcount} record has been added into database.")
        print(f"{cursor.lastrowid} is the last record id.")
    except mysql.connector.Error as e:
        print("Hata: ", e)
    finally:
        connection.close()


def insertProducts(sql_attributes, list):
    connection = mysql.connector.connect(host="localhost", user="root", password="1234", database="node-app")
    cursor = connection.cursor()
    sql_query = f"INSERT INTO new_table({sql_attributes}) VALUES (%s,%s,%s,%s)"
    cursor.executemany(sql_query, list)
    try:
        connection.commit()
        print(f"{cursor.rowcount} record has been added into database.")
        print(f"{cursor.lastrowid} is the last record id.")
    except mysql.connector.Error as e:
        print("Hata: ", e)
    finally:
        connection.close()


list = []
while True:
    name = input("Enter product name: ")
    price = int(input("Enter product price: "))
    imageUrl = input("Enter product imageUrl: ")
    description = input("Enter product description: ")
    list.append((name, price, imageUrl, description))
    choose = input("Do you want to go on[y] or exit[n] ? ")
    if choose == "n":
        print("Your record is transferring into database...")
        sql_attributes = 'name,price,imageUrl,description'
        insertProducts(sql_attributes, list)
        break
