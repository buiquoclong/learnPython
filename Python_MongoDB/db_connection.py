# db.py
# Import MongoClient từ pymongo
from pymongo import MongoClient

# Hàm lấy kết nối đến database
def get_database():
    # Thay đổi tên database tại đây nếu cần
    db_name = "mydatabase"

    # Tạo kết nối client
    client = MongoClient("mongodb://localhost:27017/")
    
    # Trả về đối tượng database
    return client[db_name]