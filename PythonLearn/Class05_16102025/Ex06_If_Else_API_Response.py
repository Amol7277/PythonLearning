# You receive an API response code from your test script.
# Write an if-else block to check whether the response is successful (status code 200) or not.

code = int(input("API response = ").strip())

if code != 200 and code != 404 and code != 404 and code != 503:
    print("The API response is not valid")
else:
    if code == 200:
        print("API response is OK")
    elif code == 404:
        print("API response not found")
    elif code == 400:
        print("API response is Bad Request")
    elif code == 503:
        print("API response is Service Unavailable")

# print("OK" if code == 200 else "Bad Request")
