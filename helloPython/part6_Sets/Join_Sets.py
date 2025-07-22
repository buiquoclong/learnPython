set1 = {1, 2, 3, 4 }
set2 = {3, 4, 5, 6 }
joined_set = set1.union(set2)  # Hợp nhất hai tập hợp và loại bỏ các phần tử trùng lặp
print("Joined Set:", joined_set)  # Kết quả: {1, 2, 3, 4, 5, 6}

result_set = set1.intersection(set2)  # Tìm giao của hai tập hợp
print("Intersection Set:", result_set)  # Kết quả: {3, 4}

result_set3 = set1 & set2  # Tương đương với phép giao, kết quả là {3, 4}
print("Intersection using & operator:", result_set3)  # Kết quả: {3, 4}

result_set1 = set1.difference(set2)  # Tìm hiệu của hai tập hợp
print("Difference Set:", result_set1)  # Kết quả: {1, 2}

result_set2 = set1 | set2  # Tương đương với phép hợp, kết quả là {1, 2, 3, 4, 5, 6}
print("Union using | operator:", result_set2)  # Kết quả: {1, 2, 3, 4, 5, 6}

