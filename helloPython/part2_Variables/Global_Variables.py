# Global Variables là biến có phạm vi toàn cục, có thể được truy cập và sửa đổi từ bất kỳ đâu trong chương trình.
# Chúng thường được sử dụng để lưu trữ các giá trị mà cần được truy cập
global_var = "I am the global"
# This is a global variable
# Khai báo function để sửa đổi biến toàn cục
def modify_global():
    # Hàm này sẽ sửa đổi biến toàn cục
    global global_var
    global_var = "I am the modified global"

# Gọi hàm để sửa đổi biến toàn cục
modify_global()
# In ra giá trị của biến toàn cục sau khi sửa đổi
print(global_var)