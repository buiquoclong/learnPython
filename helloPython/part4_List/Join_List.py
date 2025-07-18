list1 = [1, 2, 3]
list2 = ["a", "b", "c"]

joined_list = list1 + list2  # Nối hai danh sách
print("Joined list:", joined_list)

extended_list = list1 + ["x", "y", "z"]  # Nối một danh sách với một danh sách khác
print("Extended list:", extended_list)

list1.extend(list2)  # Mở rộng list1 bằng các phần tử của list2
print("List1 after extending with List2:", list1)

list2.extend(list1)  # Mở rộng list2 bằng các phần tử của list1
print("List2 after extending with List1:", list2)

repeated_list = list1 * 2  # Nhân đôi các phần tử trong list1
print("Repeated list:", repeated_list)

list1.append("new_item")  # Thêm một phần tử mới vào cuối list1
print("List1 after appending a new item:", list1)