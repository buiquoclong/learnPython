# Kết nối đến Database và thực hiện lệnh tạo Table
# import hàm từ db_connection
from db_connection import get_db_connection

# Lấy kết nối
mydb = get_db_connection()

# Tạo con trỏ truy vấn từ kết nối mydb
mycursor = mydb.cursor()

# Thực hiện lệnh tạo table
mycursor.execute("CREATE TABLE accounts(" \
                "id bigint NOT NULL AUTO_INCREMENT, " \
                "email varchar(255) NULL DEFAULT NULL, " \
                "name varchar(255) NULL DEFAULT NULL, " \
                "password varchar(255) NULL DEFAULT NULL, " \
                "phone varchar(255) NULL DEFAULT NULL, " \
                "verify_token varchar(255) NULL DEFAULT NULL, " \
                "created_at datetime(6) NULL DEFAULT NULL, " \
                "role varchar(255) NULL DEFAULT NULL, " \
                "status varchar(255) NULL DEFAULT NULL, " \
                "type varchar(255) NULL DEFAULT NULL, " \
                "updated_at datetime(6) NULL DEFAULT NULL, " \
                "username varchar(255) NULL DEFAULT NULL, " \
                "PRIMARY KEY (id) USING BTREE)")

# Hiển thị các table hiện có trong database 
mycursor.execute("SHOW TABLES")
for table in mycursor:
    print(table)