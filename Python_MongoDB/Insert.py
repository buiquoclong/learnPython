# Lấy phương thức get_database từ lớp connection
from db_connection import get_database

# Lấy đối tượng database
db = get_database()

# Tạo Collection(Bảng)
collection_name = "accounts"
# Gọi collection  (có thể tạo mới collection)
collection = db[collection_name]

# Thêm một bản ghi để "kích hoạt" collection
# Thêm document(Row) để insert
document1 = {"username": "longa", "email": "longa@example.com", "phone": "123456789", "address":"TPHCM", "age": 22}
document1 = {"username": "longa", "email": "longa@example.com", "phone": "123456789", "address":"TPHCM"}
document2 = {"username": "Trang", "email": "trang@example.com", "phone": "123456789", "address":"TPHCM"}
document3 = {"username": "Nguye", "email": "nguyen@example.com", "phone": "123456789", "address":"TPHCM"}
collection.insert_one(document1)
collection.insert_one(document2)
collection.insert_one(document3)

print("Document Inserted Successfully!")

# Lấy danh sách các data có trong Collection(Bảng)
all_document = collection.find()
for doc in all_document:
    print("Document: ", doc)

