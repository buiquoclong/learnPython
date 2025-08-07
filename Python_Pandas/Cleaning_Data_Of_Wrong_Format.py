# Nhập thư viện pandas để xử lý dữ liệu
import pandas as pd

# Tạo một DataFrame giả lập với dữ liệu đầu vào có định dạng sai ở cột "Price"
data_wrong_formats = {
    "ProductID": ["P001", "P002", "P003", "P004"],           # Mã sản phẩm
    "Price": ["50.25$", "45.50$", "60.00#", "35.75$"]        # Giá có chứa ký tự đặc biệt không hợp lệ
}

# Chuyển dictionary thành DataFrame
df_wrong_formats = pd.DataFrame(data_wrong_formats)

# Định nghĩa hàm làm sạch dữ liệu trong cột "Price"
def clean_price(price):
    # Giữ lại các ký tự là số và dấu chấm trong chuỗi (loại bỏ ký tự như $, #, v.v.)
    clean_str = ''.join(ch for ch in price if ch.isdigit() or ch == '.')
    return float(clean_str)  # Chuyển chuỗi sạch thành số thực (float)

# Áp dụng hàm làm sạch lên toàn bộ cột "Price"
df_wrong_formats["Price"] = df_wrong_formats["Price"].apply(clean_price)

# In kết quả sau khi làm sạch
print("\nCleaning data - Removing symbols:")
print(df_wrong_formats)
