my_set = {1, 2, 3, 4, 5}  # Creating a set

for item in my_set:  # Looping through the set
    print("Item:", item)  # Output each item in the set

my_set2 = {10, 20, 30, 40, 50}  # Another set
for index, value in enumerate(my_set2):  # Looping with index, enumerate dùng để lặp qua các phần tử và đồng thời trả về chỉ số của chúng
    print(f"Index: {index}, Value: {value}")  # Output index and value

for item in my_set:
    if item % 2 == 0:  # Check if the item is even
        print(f"Even Item: {item}")  # Output only even items
    else:
        print(f"Odd Item: {item}")  # Output odd items

while my_set:  # Chạy vòng lặp cho đến khi tập hợp rỗng
    item = my_set.pop()  # Xóa và trả về một phần tử ngẫu nhiên từ tập hợp
    print(f"Popped Item: {item}")  # Output the popped item