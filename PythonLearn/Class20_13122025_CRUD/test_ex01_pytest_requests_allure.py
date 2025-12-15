import pytest
import requests
import allure

@allure.title("Get Response code")
@allure.description("My get requests response and status code")
@pytest.mark.scode
def test_status_code():
    response = requests.get("https://restful-booker.herokuapp.com/booking/1")
    assert response.status_code == 200
    # a = response.json()
    # print(response.status_code)

