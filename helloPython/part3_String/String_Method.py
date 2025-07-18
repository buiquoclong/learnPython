text_message = "Python programming"

# In hoa đoạn văn bản
text_upper = text_message.upper()
# In thường đoạn văn bản
text_lower = text_message.lower()
# Chuyển đổi đoạn văn bản thành chữ hoa đầu mỗi từ
text_title = text_message.title()
# Chữ hoa đầu câu
text_capitalize = text_message.capitalize()
# Đảo ngược chữ hoa và chữ thường
text_swapcase = text_message.swapcase()

message = "Hello, World!"
# Thay thế từ "World" bằng "Python"
new_message = message.replace("World", "Python")

print("Original text:", text_message)
print("Uppercase:", text_upper)
print("Lowercase:", text_lower)
print("Title case:", text_title)
print("Capitalized:", text_capitalize)
print("Swap case:", text_swapcase)

word = "Python123"
is_alpha = word.isalpha()  # Kiểm tra xem có phải là chữ cái không
is_digit = word.isdigit() # Kiểm tra xem có phải là chữ số không(chấp nhận ít loại số như số nguyên, số thập phân, v.v.)
is_numeric = word.isnumeric() # Kiểm tra xem có phải là số không(châp nhận nhiều loại số như số thập phân, số La Mã, v.v.)

print("The word is:", word)
print("Is alpha:", is_alpha)
print("Is digit:", is_digit)
print("Is numeric:", is_numeric)