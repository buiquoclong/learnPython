# Lấy phương thức get_database từ lớp connection
from db_connection import get_database

# Lấy đối tượng database
db = get_database()

# Tạo Collection(Bảng)
collection_name = "accounts"
# Gọi collection  (có thể tạo mới collection)
collection = db[collection_name]


# Lấy danh sách data theo điều kiện có address
query = {"address": "SaiGon"}
# Lấy có chọn lọc các trường trong Collection 1 là lấy, 0 là không lấy trong Collection
Projection = {"username": 1, "address": 1, "_id": 0} 
result = collection.find(query, Projection)

for re in result:
    print("Data with condition: ", re)

