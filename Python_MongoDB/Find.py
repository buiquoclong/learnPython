# Lấy phương thức get_database từ lớp connection
from db_connection import get_database

# Lấy đối tượng database
db = get_database()

# Tạo Collection(Bảng)
collection_name = "accounts"
# Gọi collection  (có thể tạo mới collection)
collection = db[collection_name]

# Lấy danh sách các data có trong Collection(Bảng)
all_document = collection.find()
for doc in all_document:
    print("Document: ", doc)

# Lấy danh sách data theo điều kiện có address
query = {"address": "SaiGon"}
result = collection.find(query)

for re in result:
    print("Data with condition: ", re)


# Lấy danh sách data theo điều kiện có age
# Sử dụng toán tử so sánh
# "$gt": > (greater than)
# "$lt": < (less than)
# "$gte": >= 
# "$lte": <=
# "$eq": =
# "$ne": != (not equal)
query = {"age": {"$gt": 22}} # lấy các dòng có age > 22
result1 = collection.find(query)

for re in result1:
    print("Data with condition age: ", re)