import requests

try:
    url = input("Enter the URL: ")
    response = requests.get(url, timeout = 3)
    print(response.status_code)

except requests.exceptions.ConnectionError:
    print("Entered Invalid URL")

except requests.exceptions.Timeout:
    print("Time out error")

except Exception as f:
    print(f)
