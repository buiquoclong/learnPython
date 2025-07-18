list = ["math", "chemistry", 1997, 2000]
list.append(1122233)  # Thêm một phần tử mới vào cuối danh sách
print("List after appending:", list)

list.insert(2, "physics")  # Chèn một phần tử vào chỉ mục 2
print("List after inserting 'physics' at index 2:", list)

list.remove(1997)  # Xóa phần tử 1997 khỏi danh sách
print("List after removing 1997:", list)

list1 = [1,2,1,1,3,2,3,2,3,2,4]
print("Count of 1 in list1:", list1.count(1))  # Đếm số lần xuất hiện của phần tử 1
print("Count of 2 in list1:", list1.count(2))  # Đếm số lần xuất hiện của phần tử 2
print(list1.index(3))  # Tìm chỉ mục đầu tiên của phần tử 3

list2 = [2.3, 4.445, 3, 5.33, 1.54, 2.5]
list2.sort()  # Sắp xếp danh sách theo thứ tự tăng dần
print("Sorted list2:", list2)
list2.sort(reverse=True)  # Sắp xếp danh sách theo thứ tự giảm dần
print("Sorted list2 in descending order:", list2)   

print(list2.pop())  # Xóa và trả về phần tử cuối cùng của danh sách

list2.remove(3)  # Xóa phần tử 3 khỏi danh sách
print("List2 after removing 3:", list2)