import pandas as pd

# Dữ liệu đầu vào có định dạng sai
data_wrong_formats = {
    "ProductID": ["P001", "P002", "P003", "P004"],
    "Price": ["50.25$", "45.50$", "60.00#", "35.75$"]
}

df_wrong_formats = pd.DataFrame(data_wrong_formats)

# Hàm làm sạch ký tự không mong muốn khỏi cột Price
def clean_price(price):
    # Giữ lại các ký tự số và dấu chấm
    clean_str = ''.join(ch for ch in price if ch.isdigit() or ch == '.')
    return float(clean_str)

# Áp dụng làm sạch lên cột Price
df_wrong_formats["Price"] = df_wrong_formats["Price"].apply(clean_price)

# In kết quả
print("\nCleaning data - Removing symbols:")
print(df_wrong_formats)
