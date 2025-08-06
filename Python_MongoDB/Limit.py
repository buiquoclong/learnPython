# Import phương thức get_database từ module db_connection
from db_connection import get_database

# Lấy đối tượng database từ phương thức get_database
db = get_database()

# Đặt tên collection (tương đương với bảng trong SQL)
collection_name = "accounts"

# Truy cập collection có tên "accounts" trong database (nếu chưa có sẽ được tạo mới)
collection = db[collection_name]

# --------------------- LẤY DỮ LIỆU GIỚI HẠN ---------------------

# Truy vấn: lấy 5 document đầu tiên trong collection
result1 = collection.find().limit(5)
# Duyệt qua và in ra từng document trong kết quả
for doc_limit in result1:
    print("Data:", doc_limit)

# Truy vấn: bỏ qua 2 document đầu tiên và lấy 5 document tiếp theo
result2 = collection.find().skip(2).limit(5)
# Duyệt qua và in ra từng document trong kết quả
for doc_limit in result2:
    print("Data:", doc_limit)

# --------------------- PHÂN TRANG DỮ LIỆU ---------------------

# Thiết lập số lượng document hiển thị mỗi trang
pagesize = 5

# Nhập số trang muốn xem từ người dùng
page_input = input("Please enter your page: ")

# Kiểm tra xem người dùng có nhập số hợp lệ hay không
if page_input.isdigit():
    # Chuyển đổi input thành số nguyên và trừ 1 để phù hợp với chỉ số (index bắt đầu từ 0)
    page = int(page_input) - 1

    # Hiển thị vị trí bắt đầu của dữ liệu cần truy xuất (chỉ để debug)
    print(page * pagesize)

    # Truy vấn: bỏ qua số document tương ứng với số trang và lấy pagesize document tiếp theo
    result2 = collection.find().skip(page * pagesize).limit(pagesize)

    # Duyệt qua và in ra từng document trong kết quả
    for doc_limit in result2:
        print("Data:", doc_limit)
else:
    # Thông báo nếu người dùng nhập không hợp lệ
    print("Invalid input. Please enter a number")
