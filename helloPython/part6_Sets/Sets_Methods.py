# Sets Method là một phần của Python cho phép bạn làm việc 
# với các tập hợp (sets) - một kiểu dữ liệu không có thứ tự và không chứa các phần tử trùng lặp. 
# Dưới đây là một số phương thức cơ bản để thao tác với sets.
# Tạo một tập hợp
my_set = {1, 2, 3, 4, 5}  # Tạo một tập hợp
print("Original Set:", my_set)  # In tập hợp ban đầu
# Thêm phần tử vào tập hợp
my_set.add(6)  # Thêm phần tử 6 vào tập hợp 
print("Set after adding 6:", my_set)  # In tập hợp sau khi thêm phần tử
# Xóa phần tử khỏi tập hợp  
my_set.remove(3)  # Xóa phần tử 3 khỏi tập hợp
print("Set after removing 3:", my_set)  # In tập hợp sau khi x
my_set.update([7, 8])  # Thêm nhiều phần tử vào tập hợp
print("Set after updating with [7, 8]:", my_set)  # In tập hợp sau khi cập nhật
# Kiểm tra phần tử có trong tập hợp hay không
print("Is 4 in the set?", 4 in my_set)  # Kiểm tra xem 4 có trong tập hợp không
print("Is 10 in the set?", 10 in my_set)  # Kiểm tra xem 10 có trong tập hợp không
# Lấy kích thước của tập hợp   
print("Size of the set:", len(my_set))  # In kích thước của tập hợp
# Xóa tất cả phần tử khỏi tập hợp
my_set.clear()  # Xóa tất cả phần tử khỏi tập hợp   
print("Set after clearing:", my_set)  # In tập hợp sau khi xóa tất cả phần tử

my_set.discard(2)  # Xóa phần tử 2 khỏi tập hợp nếu nó tồn tại, không
print("Set after discarding 2:", my_set)  # In tập hợp sau khi xóa phần tử

my_set1 = {30, 60, 90}
my_set1.update({10, 20, 50}) # Cập nhật tập hợp với các phần tử mới
print("Set after updating with {10, 20, 50}:", my_set1)  # In tập hợp sau khi cập nhật, có thể không đúng thứ tự