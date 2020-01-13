import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host = 'localhost', database = 'demo', user = 'root', password = 'freshworks')

    if connection.is_connected():
        db_info = connection.get_server_info
        print("connected to mysql server version ", db_info)
        cursor = connection.cursor()
        #cursor.execute("create table users(id int(20) PRIMARY KEY AUTO_INCREMENT, name varchar(50) NOT NULL);")

        #n = int(input("Enter the no. of rows you want to insert"))

        #for i in  range(n):
        #val = input("Enter the value you want to insert")
        query = "insert into users(name) values('mr7');"
        cursor.execute(query)
        connection.commit()

    cursor.execute("select * from users;")
    print(cursor.fetchall())

except Error as e:
    print("Error connecting Mysql",e)

finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("Mysql connection closed")