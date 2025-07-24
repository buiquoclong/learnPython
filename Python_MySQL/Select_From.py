# Kết nối đến Database và thực hiện truy vấn dữ liệu với SELECT FROM
# import hàm từ db_connection
from db_connection import get_db_connection

# Lấy kết nối
mydb = get_db_connection()

# Tạo con trỏ truy vấn từ kết nối mydb
mycursor = mydb.cursor()

# Thực thi lệnh SELECT để lấy tất cả dữ liệu từ bẳng
mycursor.execute("SELECT * FROM accounts")

list_accounts = mycursor.fetchall()
for acc in list_accounts:
    print(acc)

# Thực thi lệnh SELECT để lấy một số trường của tất cả dữ liệu từ bảng
mycursor.execute("SELECT email, name FROM accounts")
list = mycursor.fetchall()
for i in list:
    print(i)

# Thực thi lệnh SELECT để lấy một dữ liệu từ bảng
mycursor.execute("SELECT * FROM accounts")
acc = mycursor.fetchone()
print(acc)