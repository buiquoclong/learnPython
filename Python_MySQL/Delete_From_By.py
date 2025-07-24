# Kết nối đến Database và thực hiện truy vấn dữ liệu hoặc xóa
# import hàm từ db_connection
from db_connection import get_db_connection

# Lấy kết nối
mydb = get_db_connection()

# Tạo con trỏ truy vấn từ kết nối mydb
mycursor = mydb.cursor()

# Câu lệnh SQL cần thực thi
sql = "DELETE FROM accounts WHERE username = 'eve_white'"
sql1 = "DELETE FROM accounts WHERE username = %s"
name = "abc"

# Thực thi câu lệnh DELETE để xóa dữ liệu theo điều kiện
mycursor.execute(sql)
# mycursor.execute(sql1, name)

# Lưu thay đổi vào database
mydb.commit()

# In ra kết quả insert
print(mycursor.rowcount, "record(s) deleted.")