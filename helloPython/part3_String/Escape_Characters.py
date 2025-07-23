# Escape Character là các ký tự đặc biệt trong chuỗi Python, 
# được sử dụng để biểu diễn các ký tự không thể nhập trực tiếp hoặc có ý nghĩa đặc biệt. 
# Ví dụ, `\n` đại diện cho ký tự xuống dòng, `\t` đại diện cho tab, và `\\` đại diện cho dấu gạch chéo ngược.

# Một câu có chứ ký tự xuống dòng
line_message = "This is line 1\nThis is line 2\nThis is line 3"

# Một câu có chứ ký tự tab
# Tab được sử dụng để căn chỉnh văn bản
tab_message = "Column 1\tColumn 2\tColumn 3"

# Một câu có chứ ký tự đặc biệt là ký hiệu tiền tệ
# Ký hiệu tiền tệ thường được sử dụng để biểu diễn giá trị tiền tệ
symbol_message = "This is a European symbol: \u20AC"

print(line_message)
print(tab_message)
print(symbol_message)