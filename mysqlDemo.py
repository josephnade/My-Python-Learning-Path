import mysql.connector


def insertProduct(sql_attributes, values):
    connection = mysql.connector.connect(host="localhost", user="root", password="1234", database="node-app")
    cursor = connection.cursor()
    sql_query = f"INSERT INTO new_table({sql_attributes}) VALUES (%s,%s,%s,%s,%s)"
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
    sql_query = f"INSERT INTO new_table({sql_attributes}) VALUES (%s,%s,%s,%s,%s)"
    cursor.executemany(sql_query, list)
    try:
        connection.commit()
        print(f"{cursor.rowcount} record has been added into database.")
        print(f"{cursor.lastrowid} is the last record id.")
    except mysql.connector.Error as e:
        print("Hata: ", e)
    finally:
        connection.close()


def getProducts(sql_attributes, min_price=-1, max_price=-1, name_word="", desc_word="", categoryid=-1):
    connection = mysql.connector.connect(host="localhost", user="root", password="1234", database="node-app")
    cursor = connection.cursor()
    if min_price >= 0 and max_price >= 0:
        cursor.execute(
            f"SELECT {sql_attributes} FROM new_table WHERE price <= {max_price} and price >= {min_price} ORDER BY price DESC")
    if len(name_word) > 0:
        cursor.execute(f"SELECT {sql_attributes} FROM new_table WHERE name LIKE '%{name_word}%' ORDER BY price DESC")
    if len(desc_word) > 0:
        cursor.execute(
            f"SELECT {sql_attributes} FROM new_table WHERE description LIKE '%{desc_word}%' ORDER BY price DESC")
    if categoryid > 0:
        cursor.execute(f"SELECT new_table.name,new_table.price,new_table.description,"
                       f"categories.name FROM new_table INNER JOIN categories on categories.id = new_table.categoryid WHERE categories.id = {categoryid}")
    result = cursor.fetchall()
    return result


def getProductInfo():
    connection = mysql.connector.connect(host="localhost", user="root", password="1234", database="node-app")
    cursor = connection.cursor()
    choose = input(
        "[0]Count\n[1]Minimum price\n[2]Maximum price\n[3]Average Price\n[4]Summary of Price\nWhat do you want to do: ")
    if choose == "0":
        cursor.execute("SELECT COUNT(*) FROM new_table")
        result = cursor.fetchone()
        print(f"Count: {result[0]}")
    if choose == "1":
        cursor.execute("SELECT MIN(price) FROM new_table")
        result = cursor.fetchone()
        print(f"Minimum Price: {result[0]}")
    if choose == "2":
        cursor.execute("SELECT MAX(price) FROM new_table")
        result = cursor.fetchone()
        print(f"Maximum Price: {result[0]}")

    if choose == "3":
        cursor.execute("SELECT AVG(price) FROM new_table")
        result = cursor.fetchone()
        print(f"Average Price: {result[0]}")
    if choose == "4":
        cursor.execute("SELECT SUM(price) FROM new_table")
        result = cursor.fetchone()
        print(f"Summary of Price: {result[0]}")


def updateProduct(change, id):
    connection = mysql.connector.connect(host="localhost", user="root", password="1234", database="node-app")
    cursor = connection.cursor()
    sql = f"UPDATE new_table SET name ='{change}' WHERE id = {id}"
    cursor.execute(sql)
    try:
        connection.commit()
        print("Updating is successfull")
    except mysql.connector.Error as e:
        print("Hata: ", e)
    finally:
        connection.close()


def deleteProduct(id):
    connection = mysql.connector.connect(host="localhost", user="root", password="1234", database="node-app")
    cursor = connection.cursor()
    sql_query = f"DELETE FROM new_table WHERE id = {id}"
    cursor.execute(sql_query)
    try:
        connection.commit()
        print("Data has been deleted!")
    except mysql.connector.Error as e:
        print("Hata: ", e)
    finally:
        connection.close()


def innerJoin():
    connection = mysql.connector.connect(host="localhost", user="root", password="1234", database="node-app")
    cursor = connection.cursor()
    sql = f"SELECT * FROM new_table INNER JOIN categories on categories.id = new_table.categoryid"
    cursor.execute(sql)
    try:
        result = cursor.fetchall()
        for product in result:
            print(f"Name: {product[1]} | Price: {product[2]} | description: {product[4]} | Category Id: {product[5]} |"
                  f"Category Name: {product[7]}")
    except mysql.connector.Error as e:
        print(e)
    finally:
        connection.close()


list = []
sql_attributes = 'name,price,imageUrl,description,categoryid'
while True:
    option = input(
        "[1] Insert data into database\n[2]- Get data from database\n[3]Aggregiate Function(Min-Max-Avg-Sum)\n"
        "[4]Update data using id\n[5]Delete data using id\n[6]- Joins\n[q]- Exit\nWhat do you want to do:")
    if option == "1":
        name = input("Enter product name: ")
        price = int(input("Enter product price: "))
        imageUrl = input("Enter product imageUrl: ")
        description = input("Enter product description: ")
        categoryid = int(input("Enter category id: "))
        list.append((name, price, imageUrl, description, categoryid))
        choose = input("Do you want to go on[y] or exit[n] ? ")
        if choose == "n":
            print("Your record is transferring into database...")
            insertProducts(sql_attributes, list)
            break
    if option == "2":
        filtering = input(
            "[1]- name\n[2]- price\n[3]- description\n[4]- Category id\nWhich attribute do you want to filter:")
        if filtering == "1":
            name_word = input("Search word for name attribute: ")
            result = getProducts(sql_attributes, name_word=name_word)
        if filtering == "2":
            min_price = int(input("Please enter the minimum price:"))
            max_price = int(input("Please enter the maximum price:"))
            result = getProducts(sql_attributes, min_price=min_price, max_price=max_price)
        if filtering == "3":
            desc_word = input("Search word for description attribute:")
            result = getProducts(sql_attributes, desc_word=desc_word)
        if filtering == "4":
            categoryId = int(input("Please enter the category id: "))
            inner = getProducts(sql_attributes, categoryid=categoryId)
            result = []
            for x in inner:
                print(
                    f"Name: {x[0]} | Price = {x[1]} | Description = {x[2]} | Catogory Name = {x[3]}")
        if len(result) == 0:
            continue
        else:
            for x in result:
                print(f"Name: {x[0]} | Price = {x[1]} | imageUrl = {x[2]} | description = {x[3]} | category id = {x[4]}")
    if option == "3":
        getProductInfo()
    if option == "4":
        id = int(input("Please enter an ID: "))
        change = input("Please enter the value you want to change: ")
        updateProduct(change, id)
    if option == "5":
        id = int(input("Please enter an ID: "))
        deleteProduct(id)
    if option == "6":
        filtering = input("[1]- Inner Join\n [2]- Left Join\n[3]- Right Join\n[4]-Outer Join\nWhat do you want to do: ")
        if filtering == "1":
            innerJoin()
    if option == "q":
        print("Have a good day!")
        break
