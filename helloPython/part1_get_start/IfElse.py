# Example 1:
print("Example 1:")
age = 15

# Kiểm tra nếu tuổi lớn hơn hoặc bằng 18 thì in ra "you are a adult", ngược lại in ra "you are a minor"
if age >= 18:
    print("you are a adult")
else:
    print("you are a minor")
print("----------------------------------------------------------")
# Example 2:
print("Example 2:")
score = 75

# Kiểm tra điểm số và in ra xếp loại tương ứng
# Nếu điểm số >= 90 thì in ra "A", nếu điểm số >= 80 thì in ra "B", nếu điểm số >= 70 thì in ra "C", ngược lại in ra "You need improvement"
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("You need improvement")