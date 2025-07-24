# Kết nối đến Database và thực hiện lệnh thêm dữ liệu vào Table

# import hàm từ db_connection
from db_connection import get_db_connection

# Lấy kết nối
mydb = get_db_connection()

# Tạo con trỏ truy vấn từ kết nối mydb
mycursor = mydb.cursor()

# Câu lệnh INSERT
sql = """
    INSERT INTO accounts (
        email, name, password, phone, verify_token, 
        created_at, role, status, type, updated_at, username
    ) 
    VALUES (
        %s, %s, %s, %s, %s, 
        NOW(), %s, %s, %s, NOW(), %s
    )
"""

# Dữ liệu để chèn vào
val1 = (
    'example@email.com', 'John Doe', 'password123', '1234567890', 'some_token',
    'user', 'active', 'regular', 'john_doe'
)
val2 = [
    ('alice@email.com', 'Alice Smith', 'alice123', '0987654321', 'token1', 'user', 'active', 'premium', 'alice_smith'),
    ('bob@email.com', 'Bob Johnson', 'bob123', '1122334455', 'token2', 'user', 'inactive', 'regular', 'bob_johnson'),
    ('charlie@email.com', 'Charlie Brown', 'charlie123', '2233445566', 'token3', 'admin', 'active', 'admin', 'charlie_brown'),
    ('david@email.com', 'David Lee', 'david123', '3344556677', 'token4', 'user', 'active', 'regular', 'david_lee'),
    ('eve@email.com', 'Eve White', 'eve123', '4455667788', 'token5', 'user', 'inactive', 'regular', 'eve_white')
]

# Thực thi lệnh INSERT
mycursor.execute(sql, val1) # Insert một dòng dữ liệu
mycursor.executemany(sql, val2)

# Lưu thay đổi vào database
mydb.commit()

# In ra kết quả insert
print(mycursor.rowcount, "record(s) inserted.")