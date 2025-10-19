# An API sometimes fails due to network delays.
#
# Write a program to retry the API call 3 times until the response code becomes 200.
#
# If it still fails after 3 tries, print a failure message.
#
# Hint: Use a while loop with a counter.
#
# Expected Output Example:
#
# Attempt 1: Response 500
#
# Attempt 2: Response 200
#
# ✅ Test Passed

i = 0
while i < 3:
    AT = int(input("Response Code: "))
    if AT == 200:
        print("✅ Test Passed")
        break
    elif AT != 200:
        print("Response not correct, try again")
    i = i + 1

if i == 3:
    print("Too many attempts! Please Try after 24 hours.")