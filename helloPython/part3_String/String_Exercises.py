# Đảo ngược chuỗi
def reverse_String(input_string):
    return input_string[::-1]
original_text = "Python programming"
reverse_text = reverse_String(original_text)
print("Original text:", original_text)
print("Reversed text:", reverse_text)

# Đếm số lượng nguyên âm trong chuỗi
def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in input_string if char in vowels) 
    character_with_vowels = [char for char in input_string if char in vowels]
    return f"the input string has {count} vowels: {character_with_vowels}"
text_with_vowels = "Python programming is fun!"
count_result = count_vowels(text_with_vowels)
print(count_result)
# vowel_count = count_vowels(text_with_vowels)
# print(f"The number of vowels in '{text_with_vowels}' is: {vowel_count}")
