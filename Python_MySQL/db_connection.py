# db_connection.py
import mysql.connector

# Hàm trả về kết nối MySQL
def get_db_connection():
    # Kết nối tới cơ sở dữ liệu 
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  
        database="testdb"  # Chỉ định tên database trong cơ sở dữ liệu
    )
    return mydb