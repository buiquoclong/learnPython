# Kết nối đến MySQL và thực hiện lệnh tạo Database
# Connect to MySQL Database
# import mysql.connector
from db_connection import get_db_connection
# Kết nối tới MySQL
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password=""
# )

# Lấy kết nối
mydb = get_db_connection()

# Tạo con trỏ truy vấn từ kết nối mydb
mycursor = mydb.cursor()

# Tạo database
# mycursor.execute("CREATE DATABASE testdb") # Đã tạo database

# Hiển thị các database hiện có trong MySQL
mycursor.execute("SHOW DATABASES")
for db in mycursor:
    print(db)
