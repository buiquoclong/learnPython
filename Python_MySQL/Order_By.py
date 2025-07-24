# Kết nối đến Database và thực hiện truy vấn dữ liệu với ORDER BY
# import hàm từ db_connection
from db_connection import get_db_connection

# Lấy kết nối
mydb = get_db_connection()

# Tạo con trỏ truy vấn từ kết nối mydb
mycursor = mydb.cursor()

# Câu lệnh SQL cần thực thi
sql1 = "SELECT * FROM accounts ORDER BY name"
sql2 = "SELECT * FROM accounts ORDER BY name ASC" # Sắp xếp theo thứ tự tăng dần
sql3 = "SELECT * FROM accounts ORDER BY name DESC" # Sắp xếp theo thứ tự giảm dần

# Thực thi lệnh SELECT để lấy tất cả dữ liệu từ bảng và sắp xếp
mycursor.execute(sql1)

result = mycursor.fetchall()

# In ra danh sách các kết quá
for acc1 in result:
    print(acc1)

# Thực thi lệnh SELECT để lấy tất cả dữ liệu từ bảng và sắp xếp theo thứ tự tăng dần
mycursor.execute(sql2)

result = mycursor.fetchall()

# In ra danh sách các kết quá theo thứ tự tăng dần
for acc2 in result:
    print(acc2)


# Thực thi lệnh SELECT để lấy tất cả dữ liệu từ bảng và sắp xếp theo thứ tự giảm dần
mycursor.execute(sql2)

result = mycursor.fetchall()

# In ra danh sách các kết quá theo thứ tự giảm dần
for acc2 in result:
    print(acc2)