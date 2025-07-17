# tạo đường dẫn của file muốn tạo
filePath = "NewCreateFile.txt"
# thực hiện thao tác mở file (open()) với nhiều chế độ khác nhau
# 'r': Read- Mở file để đọc, File phải tồn tại
# 'w': Write - Mở file để ghi, nếu file tồn tại thì ghi đè, nếu không có file thì thực hiện tạo mới file
# 'a'	Append – Mở file để ghi nối tiếp vào cuối. Nếu file không tồn tại, sẽ tạo mới.	
# 'x'	Exclusive creation – Tạo file mới. Nếu file đã tồn tại thì sẽ báo lỗi.	
# 'b'	Binary mode – Dùng cho file nhị phân (ảnh, audio, v.v.). Dùng kèm với các chế độ khác, ví dụ 'rb', 'wb'.	
# 't'	Text mode – Mặc định. Dùng cho file văn bản (chuỗi).	
# '+'	Read và Write – Cho phép đọc và ghi đồng thời. Kết hợp với 'r', 'w' hoặc 'a', ví dụ 'r+', 'w+'.

# ghi file mới với w
new_file_with_w = open(filePath, "w")
new_file_with_w.write("Hello, this is a new file after create file with w")
new_file_with_w.close()
print("Đã thực hiện ghi file mới")
print("---------------------------------------------------------------")

# đọc file với r
read_file_with_r = open(filePath, "r")
content = read_file_with_r.read()
print(content)
read_file_with_r.close()
print("Đã thực hiện đọc file")
print("---------------------------------------------------------------")

# ghi nối tiếp file với a
continue_write_with_a = open(filePath, "a")
continue_write_with_a.write("\nGhi tiếp thêm một dòng mới")
continue_write_with_a.close()
print("Đã thực hiện ghi nối tiếp")
print("---------------------------------------------------------------")