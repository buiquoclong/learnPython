# Kết nối đến Database và thực hiện truy vấn dữ liệu từ table sử dụng join
# import hàm từ db_connection
from db_connection import get_db_connection

# Lấy kết nối
mydb = get_db_connection()

# Tạo con trỏ truy vấn từ kết nối mydb
mycursor = mydb.cursor()

# Câu lệnh SQL cần thực thi
sql = "SELECT a.name FROM accounts a INNER JOIN usernames u ON u.id = a.id"
sql2 = "SELECT a.name FROM accounts a RIGHT JOIN usernames u ON u.id = a.id"
sql3 = "SELECT a.name FROM accounts a LEFT JOIN usernames u ON u.id = a.id"

# Thực thi lệnh SELECT để lấy dữ liệu từ bảng từ câu sql INNER JOIN
mycursor.execute(sql)

list_accounts = mycursor.fetchall()
for acc in list_accounts:
    print(acc)
print("------------------------------------------------")
# Thực thi lệnh SELECT để lấy dữ liệu từ bảng từ câu sql2 RIGHT JOIN
mycursor.execute(sql2)

list_accounts2 = mycursor.fetchall()
for acc in list_accounts2:
    print(acc)


print("------------------------------------------------")
# Thực thi lệnh SELECT để lấy dữ liệu từ bảng từ câu sql3 LEFT JOIN
mycursor.execute(sql3)

list_accounts3 = mycursor.fetchall()
for acc in list_accounts3:
    print(acc)