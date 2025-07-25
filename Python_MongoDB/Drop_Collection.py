# Lấy phương thức get_database từ lớp connection
from db_connection import get_database

# Lấy đối tượng database
db = get_database()

# Tạo Collection(Bảng)
collection_name = "accounts"
# Gọi collection  (có thể tạo mới collection)
collection = db[collection_name]

# Thực hiện drop Collection(Table) cần drop
collection.drop()