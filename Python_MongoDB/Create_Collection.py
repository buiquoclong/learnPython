# Lấy phương thức get_database từ lớp connection
from db_connection import get_database

# Lấy đối tượng database
db = get_database()

# Tạo Collection(Bảng)
collection_name = "accounts"
collection = db[collection_name]

# Thêm một bản ghi để "kích hoạt" collection
collection.insert_one({"username": "long", "email": "long@example.com", "phone": "123456789", "address":"TPHCM"})

print("Collection Created: ", collection_name)

existing_collection = db.list_collection_names()
print("Existing Collection: ", existing_collection)