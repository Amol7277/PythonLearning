num = int(input("Enter a number: "))
reverse = 0

while num > 0:
    digit = num % 10          # Get the last digit          reminder 4
    reverse = reverse * 10 + digit  # Add it to the reversed number   4
    num = num // 10           # Remove the last digit             quicient = 123

print("Reversed number:", reverse)