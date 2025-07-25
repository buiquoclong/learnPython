# Lấy phương thức get_database từ lớp connection
from db_connection import get_database
import pymongo

# Lấy đối tượng database
db = get_database()

# Tạo Collection(Bảng)
collection_name = "accounts"
# Gọi collection  (có thể tạo mới collection)
collection = db[collection_name]

# Thực hiện tìm kiếm và sắp xếp theo thứ tự tăng dần
sort_order_asc = [("address", pymongo.ASCENDING)]
result_asc = collection.find().sort(sort_order_asc)

for doc in result_asc:
    print("Document ASCENDING: ", doc)

print("----------------------------------------")
# Thực hiện tìm kiếm và sắp xếp theo thứ tự giảm dần
sort_order_desc = [("address", pymongo.DESCENDING)]
result_desc = collection.find().sort(sort_order_desc)

for doc in result_desc:
    print("Document DESCENDING: ", doc)


print("----------------------------------------")
# Thực hiện tìm kiếm và sắp xếp nhiều cột
mult_sort_order = [("username", pymongo.ASCENDING), ("address", pymongo.DESCENDING)]
result_mult_sort = collection.find().sort(mult_sort_order)

for doc in result_mult_sort:
    print("Document Multi Sort: ", doc)