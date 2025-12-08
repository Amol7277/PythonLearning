try:
    data = open("Test.json").read()

# except FileNotFoundError as f:
#     print(f)

except FileNotFoundError:
    print("File Not Found")