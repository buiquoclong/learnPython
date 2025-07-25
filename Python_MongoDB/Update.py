# Lấy phương thức get_database từ lớp connection
from db_connection import get_database

# Lấy đối tượng database
db = get_database()

# Tạo Collection(Bảng)
collection_name = "accounts"
# Gọi collection  (có thể tạo mới collection)
collection = db[collection_name]

filter_query1 = {"username": "longa"} # Điều kiện data update
update_query = {"$set": {"address": "SaiGon", "email": "aaa@gmail.com"}} # thông tin data update
collection.update_one(filter_query1, update_query) # Update một dòng data
print("Document Updated Successfully")

filter_query2 = {"username": "longb"} # Điều kiện data update
update_query2 = {"$set": {"address": "SaiGon", "email": "aaab@gmail.com"}}  # thông tin data update
result = collection.update_many(filter_query2, update_query2) # Update nhiều dòng data
print("Number of Document Update Successfully: ", result.modified_count)