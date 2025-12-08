from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver

try:
    driver = webdriver.Chrome()
    driver.get("https://google.com/")
    driver.find_element("id", "Not exist button")

# except NoSuchElementException:
#     print("Element Not Found")

except NoSuchElementException as nse:
    print(nse.msg)