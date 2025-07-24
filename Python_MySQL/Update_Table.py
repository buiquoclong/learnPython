# Kết nối đến Database và thực hiện UPDATE table
# import hàm từ db_connection
from db_connection import get_db_connection

# Lấy kết nối
mydb = get_db_connection()

# Tạo con trỏ truy vấn từ kết nối mydb
mycursor = mydb.cursor()

# Câu lệnh SQL cần thực thi
sql = "UPDATE accounts SET name = 'abc' WHERE username = 'john_doe'"
sql2 = "UPDATE accounts SET name = %s WHERE username = %s"
values_for_sql2 = ("abc", "john_doe")

# Thực hiện lệnh DROP table
mycursor.execute(sql)

# Lưu thay đổi vào database
mydb.commit()

# In ra kết quả insert
print(mycursor.rowcount, "record(s) are affected.")