input_string = "hello, world!"

vowels = "aeiou"
consonant_count = 0
vowels_count = 0
consonant_list = list()
vowels_list = list()

for char in input_string:
    if char.isalpha() and char not in vowels:
        consonant_count += 1
        consonant_list.append(char)
    else:
        if char.isalpha() and char in vowels:
            vowels_count += 1
            vowels_list.append(char)

print("consonant Count ", consonant_count)
print("consonant_list ", consonant_list)

print("vowelscount ", vowels_count)
print("vowels_list ",vowels_list)
