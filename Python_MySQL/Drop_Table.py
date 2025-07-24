# Kết nối đến Database và thực hiện DROP table
# import hàm từ db_connection
from db_connection import get_db_connection

# Lấy kết nối
mydb = get_db_connection()

# Tạo con trỏ truy vấn từ kết nối mydb
mycursor = mydb.cursor()

# Câu lệnh SQL cần thực thi
sql = "DROP TABLE IF EXISTS accounts"

# Thực hiện lệnh DROP table
mycursor.execute(sql)

# Hiển thị các table hiện có trong database 
mycursor.execute("SHOW TABLES")
for table in mycursor:
    print(table)