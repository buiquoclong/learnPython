global_var = "I am the global"
# This is a global variable
def modify_global():
    # Hàm này sẽ sửa đổi biến toàn cục
    global global_var
    global_var = "I am the modified global"

modify_global()
# Accessing the global variable
print(global_var)