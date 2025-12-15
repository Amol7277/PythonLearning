import pytest
import requests
import allure

@allure.title("TC01 - Create Booking CRUD Positive")
@allure.description("create booking request")
@pytest.mark.positive
def test_create_booking():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    full_url = base_url + base_path

    headers = {"Content-Type": "application/json"}

    payload  ={
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.post(url=full_url, headers = headers, json=payload)
    print(response.text)
    assert response.status_code == 200

    response_data_json = response.json()
    print(response)