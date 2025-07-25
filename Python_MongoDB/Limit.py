# Lấy phương thức get_database từ lớp connection
from db_connection import get_database

# Lấy đối tượng database
db = get_database()

# Tạo Collection(Bảng)
collection_name = "accounts"
# Gọi collection  (có thể tạo mới collection)
collection = db[collection_name]

# Lấy giới hạn 5 phần tử trong danh sách tất cả data
result1 = collection.find().limit(5)
for doc_limit in result1:
    print("Data:", doc_limit)


# Lấy giới hạn 5 phần tử bỏ 2 dòng đầu tiên trong danh sách tất cả data
result2 = collection.find().skip(2).limit(5)
for doc_limit in result2:
    print("Data:", doc_limit)


# Lấy giới hạn số phần tử theo page và pagesize
pagesize = 5
page_input = input("Please enter your page: ")


if page_input.isdigit():
    page = int(page_input) - 1
    print(page*pagesize)
    result2 = collection.find().skip((page) * pagesize).limit(pagesize)
    for doc_limit in result2:
        print("Data:", doc_limit)
else:
    print("Invalid input. Please enter a number")

