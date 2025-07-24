# Kết nối đến Database và thực hiện truy vấn dữ liệu với WHERE
# import hàm từ db_connection
from db_connection import get_db_connection

# Lấy kết nối
mydb = get_db_connection()

# Tạo con trỏ truy vấn từ kết nối mydb
mycursor = mydb.cursor()

# Nhập tên người cần tìm kiếm
name_input = input("Hãy nhập tên người cần tìm")

# Câu lệnh SQL cần thực thi
sql = "SELECT * FROM accounts WHERE name LIKE %s"

# Thực thi câu lệnh SELECT để thực hiện tìm kiếm
mycursor.execute(sql, ('%' + name_input + '%',))

# Lấy tất cả kết quả truy vấn
result = mycursor.fetchall()

# Hiển thị kết quả
if result:
    for row in result:
        print(row)
else:
    print("Không tìm thấy kết quả nào.")