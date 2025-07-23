# Example 1: print count
count = 0
# Sử dụng vòng lặp while để in ra các số từ 0 đến 4
while count < 5:
    print(f"this is number {count}")
    count += 1

# Example 2: use whileloop to calculate the total
total = 0
# Sử dụng vòng lặp while để tính tổng các số do người dùng nhập vào
# Người dùng có thể nhập số bất kỳ, và vòng lặp sẽ tiếp tục cho đến khi người dùng nhập "exit"
while True:
    # Nhập số từ người dùng
    # Nếu người dùng nhập "exit", vòng lặp sẽ dừng lại
    user_input = input("enter a number (type 'exit' to stop)")
    
    # Kiểm tra nếu người dùng nhập "exit", thì thoát khỏi vòng lặp
    # Nếu người dùng nhập một số, thì cộng vào tổng
    if user_input.lower() == "exit":
        break
    elif user_input.isdigit():
        total += int(user_input)
        print(f"the total is {total}")
    else:
        print("Invalid input. Please enter a number")

    
