# Nhập thư viện pandas để xử lý dữ liệu
import pandas as pd

# ----------- Phần 1: Đọc dữ liệu từ file JSON -----------

# Đường dẫn đến file JSON
file_path = "team.json"

# Đọc dữ liệu từ file JSON và chuyển thành DataFrame
df = pd.read_json(file_path)

# In ra nội dung của DataFrame sau khi đọc từ JSON
print("DataFrame from json: ")
print(df)

# ----------- Phần 2: Tạo DataFrame từ dictionary có cấu trúc lồng (nested dictionary) -----------

# Dữ liệu thể hiện các chỉ số tập luyện (theo hàng, không phải theo cột như thông thường)
data = {
    "Duration": {
        "0": 60,
        "1": 59,
        "2": 60,
        "3": 45,
    }, 
    "Pulse": {
        "0": 110,
        "1": 117,
        "2": 103,
        "3": 109,
    },  
    "Maxpulse": {
        "0": 130,
        "1": 145,
        "2": 135,
        "3": 174,
    }, 
    "Calogies": {
        "0": 409,
        "1": 479,
        "2": 340,
        "3": 282,
    }, 
}

# Tạo DataFrame từ dictionary dạng lồng, pandas sẽ tự hiểu các key bên trong là chỉ số hàng
df = pd.DataFrame(data)

# In ra DataFrame vừa tạo
print(df)
