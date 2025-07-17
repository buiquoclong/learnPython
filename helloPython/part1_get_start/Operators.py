# toán tử với số 
a = 5
b = 10

addition = a + b
subtraction = a - b
multiplication = a * b
division = a/b
# chia lấy phần dư
modulo = a%b
# chia lấy phần nguyên
floor = a//b

print(f"the result of addition of {a} and {b} is: {addition}")
print(f"the result of subtraction of {a} and {b} is: {subtraction}")
print(f"the result of multiplication of {a} and {b} is: {multiplication}")
print(f"the result of division of {a} and {b} is: {division}")
print(f"the result of modulo of {a} and {b} is: {modulo}")
print(f"the result of floor of {a} and {b} is: {floor}")
print("----------------------------------------------------------")
# check true, false between two number
x = 10
y = 20

equal_to = x == y
not_equal_to = x != y

print(f"equal_to between {x} = {y} is: {equal_to}")
print(f"not_equal_to between {x} != {y} is: {not_equal_to}")

print("----------------------------------------------------------")
# logical with True and False
p = True
q = False

logical_and = p and q
logical_or = p or q
logical_not = not p

print(f"the result of logical_and between p({p}) and q({q}) is {logical_and}")
print(f"the result of logical_or between p({p}) and q({q}) is {logical_or}")
print(f"the result of logical_not of p({p}) is {logical_not}")

print("----------------------------------------------------------")

# assignment operator with number(toán tử gán)
counter = 5

# cộng thêm 2
counter += 2
print(counter)

# trừ 1
counter -= 1
print(counter)

# nhân 3
counter *= 3
print(counter)

# chia 2
counter /= 2
print (counter)

print("----------------------------------------------------------")

# bitwise (toán tử bit): thao tác trực tiếp trên dạng nhị phân của các số
a1 = 5      # dạng nhị phân: 0b0101
b1 = 3      # dạng nhị phân: 0b0011

bitwise_and = a1 & b1
bitwise_or = a1 | b1
bitwise_xor = a1 ^ b1
bitwise_not_a = ~a1

print(f"the result of bitwise_and between a({a1}) and b1({b1}) is {bitwise_and}")
print(f"the result of bitwise_or between a({a1}) and b1({b1}) is {bitwise_or}")
print(f"the result of bitwise_xor between a({a1}) and b1({b1}) is {bitwise_xor}")
print(f"the result of bitwise_not_a of a({a1}) is {bitwise_not_a}")