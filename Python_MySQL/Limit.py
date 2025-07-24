# Kết nối đến Database và thực hiện truy vấn dữ liệu từ table sử dụng OFFSET và LIMIT
# import hàm từ db_connection
from db_connection import get_db_connection

# Lấy kết nối
mydb = get_db_connection()

# Tạo con trỏ truy vấn từ kết nối mydb
mycursor = mydb.cursor()

# Câu lệnh SQL cần thực thi
sql = "SELECT * FROM accounts LIMIT 4 OFFSET 3"

# Thực thi lệnh SELECT để lấy dữ liệu từ bẳng
mycursor.execute(sql)

list_accounts = mycursor.fetchall()
for acc in list_accounts:
    print(acc)