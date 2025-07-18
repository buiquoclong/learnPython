original_list = [1, 2, 3, 4, 5]
copied_list1 = original_list.copy()  # Sao chép danh sách
copied_list2 = list(original_list)  # Sao chép danh sách bằng hàm list()
copied_list3 = original_list[:]  # Sao chép danh sách bằng slicing
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