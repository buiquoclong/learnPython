# Import MongoClient từ pymongo
from pymongo import MongoClient

# Kết nối tới MongoDB local
client = MongoClient("mongodb://localhost:27017/")

# Lấy danh sách các Database đã có
existing_database = client.list_database_names()
print("Existing Databases: ", existing_database)

# Tạo database (nếu chưa có thì Mongo sẽ tự tạo)
new_database_name = "new_db" # Đặt tên database muốn tạo
# Thực hiện lệnh tạo db nhưng nếu trong db không có gì thì nó sẽ không hiển thị trong danh sách db,
# nếu muốn hiển thị thì trong db phải thê một cái gì đó ví dụ như là Collection(Table), Document(Row), Field(Column)
# Vì Mongo là NoSQL nên không cần tạo bảng/collection trước - chỉ cần chèn dữ liệu là nó sẽ tự tạo
db = client[new_database_name] 
print("New database Created: ", new_database_name)
