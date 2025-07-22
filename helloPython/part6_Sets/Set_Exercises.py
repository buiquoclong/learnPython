# Set Exercises
def unique_element(input_list):
    return set(input_list)

my_list = [1, 2, 2, 3, 4, 5, 5]
unique_set = unique_element(my_list)  # Gọi hàm để lấy tập hợp các phần tử duy nhất
print("Unique elements in the list:", unique_set)  # In tập hợp các phần tử duy nhất

# Hàm trả về tập hợp giao các phần tử chung giữa hai tập hợp
def common_elements(set1, set2):
    return set1.intersection(set2)  # Trả về giao của hai tập hợp

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
common_set = common_elements(set_a, set_b)  # Gọi hàm để lấy giao của hai tập hợp
print("Common elements between set_a and set_b:", common_set)  # In giao của hai tập hợp

# Hàm trả về các phần tử khác nhau giữa hai tập hợp
def different_elements(set1, set2):
    return set1.difference(set2)  # Trả về hiệu của hai tập hợp

set_x = {1, 2, 3, 4}
set_y = {3, 4, 5, 6}
different_set = different_elements(set_x, set_y)  # Gọi hàm để lấy hiệu của hai tập hợp
print("Different elements between set_x and set_y:", different_set)  # In hiệu của hai tập hợp

# Hàm kiểm tra xem một tập hợp có phải là tập con của tập hợp khác hay không
def is_subset(set1, set2):
    return set1.issubset(set2)  # Kiểm tra xem set1 có phải là tập con của set2 không   

set_a = {1, 2}
set_b = {1, 2, 3, 4}
is_subset_result = is_subset(set_a, set_b)  # Gọi hàm để kiểm tra tập con
print("Is set_a a subset of set_b?", is_subset_result)  # In kết quả kiểm tra tập con   