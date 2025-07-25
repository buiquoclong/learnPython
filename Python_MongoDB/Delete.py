# Lấy phương thức get_database từ lớp connection
from db_connection import get_database
import pymongo

# Lấy đối tượng database
db = get_database()

# Tạo Collection(Bảng)
collection_name = "accounts"
# Gọi collection  (có thể tạo mới collection)
collection = db[collection_name]

# Tạo câu query cần chọn để xóa
delete_query1 = {"address": "SaiGon"}
# collection.delete_one(delete_query1) # Xóa một phần dòng data
# print("Document Deleted Successfully: ", delete_query1)

result = collection.delete_many(delete_query1) # Xóa nhiều dòng data
print("Number of Document Deleted Successfully: ", result.deleted_count)