# Example 1: print count
count = 0
while count < 5:
    print(f"this is number {count}")
    count += 1

# Example 2: use whileloop to calculate the total
total = 0
while True:
    user_input = input("enter a number (type 'exit' to stop)")
    if user_input.lower() == "exit":
        break
    elif user_input.isdigit():
        total += int(user_input)
        print(f"the total is {total}")
    else:
        print("Invalid input. Please enter a number")

    
