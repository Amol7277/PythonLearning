# In automation, you often compare expected and actual outputs.
# Write code to check if a test case passed or failed.
#
# expected_title = "Dashboard"
# actual_title = "Dashboard"

Data = "Dashboard"
Expected = str(input("Actual Result: ").strip())

if Expected == Data:
    print("Test Case is passed")

elif Expected == Data.lower() or Expected == Data.upper():
    print("Test Case is passed")

# elif Expected == Data.upper():
#     print("Test Case is passed")

else:
    print("Test Case is Failed")
