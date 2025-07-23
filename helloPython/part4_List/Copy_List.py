# Copy list là quá trình tạo một bản sao của danh sách hiện có.
# Điều này có thể hữu ích khi muốn làm việc với một bản sao mà không làm thay đổi danh sách gốc.
# Có nhiều cách để sao chép danh sách trong Python, bao gồm sử dụng phương thức copy(),
# hàm list(), slicing, hoặc các phương pháp khác.

# Khởi tạo một danh sách gốc
original_list = [1, 2, 3, 4, 5]

# Sao chép danh sách bằng phương thức copy()
# Phương thức copy() tạo một bản sao nông của danh sách, nghĩa là nó
# sao chép các phần tử của danh sách gốc nhưng không sao chép các đối tượng bên trong nếu chúng là danh sách lồng nhau.
# Nếu danh sách chứa các đối tượng phức tạp, bạn có thể cần sử dụng
copied_list1 = original_list.copy()  # Sao chép danh sách

# Sao chép danh sách bằng hàm list()
# Hàm list() cũng tạo một bản sao nông của danh sách.
# Nó tương tự như phương thức copy(), nhưng có thể được sử dụng để chuyển đổi các đối tượng khác thành danh sách.
copied_list2 = list(original_list)  # Sao chép danh sách bằng hàm list()

# Sao chép danh sách bằng slicing
# Slicing là một kỹ thuật trong Python cho phép bạn lấy một phần của danh sách.
# Khi sử dụng slicing, có thể chỉ định các chỉ mục để sao chép một phần của danh sách.
copied_list3 = original_list[:]  # Sao chép danh sách bằng slicing

# Sao chép danh sách bằng slicing với chỉ mục
# Có thể sao chép một phần của danh sách bằng cách chỉ định các chỉ mục
# Sao chép từ chỉ mục 1 đến 3 (không bao gồm 4) hoặc sao chép các phần tử cuối cùng.
copied_list4 = original_list[1:4]  # Sao chép một phần của danh sách từ chỉ mục 1 đến 3

copied_list5 = original_list[-3:]  # Sao chép ba phần tử cuối cùng của danh sách
copied_list6 = original_list[:-2]  # Sao chép danh sách trừ hai phần tử cuối cùng
copied_list7 = original_list[::2]  # Sao chép các phần tử ở chỉ mục chẵn
print("Original list:", original_list)
print("Copied list:", copied_list1)
print("Copied list using list():", copied_list2)
print("Copied list using slicing:", copied_list3)
print("Copied list from index 1 to 3:", copied_list4)
print("Copied last three elements:", copied_list5)
print("Copied list excluding last two elements:", copied_list6)
print("Copied elements at even indices:", copied_list7)