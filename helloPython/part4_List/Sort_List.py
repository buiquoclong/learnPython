# Trả về giá trị tuyểt đối của khoảng cách đến 50
def my_function(n):
    return abs(n - 50)
this_list = ["orange", "banana", "apple", "kiwi"]
this_list.sort()  # Sắp xếp danh sách theo thứ tự tăng dần
print("Sorted list:", this_list)
this_list.sort(reverse=True)  # Sắp xếp danh sách theo thứ tự giảm dần
print("Sorted list in descending order:", this_list)

this_list1 = [10, 20, 30, 40, 50]
this_list1.sort(key=my_function)  # Sắp xếp danh sách theo khoảng cách đến 50
print("Sorted list by distance to 50:", this_list1)