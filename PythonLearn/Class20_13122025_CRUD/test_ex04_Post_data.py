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

    booking_id = response_data_json["bookingid"]
    print("Booking ID = ", booking_id)
    assert booking_id is not None
    assert booking_id > 0
    assert type(booking_id) == int

    firstname = response_data_json["booking"]["firstname"]
    print("First Name = ",firstname)
    assert firstname == "Jim"
    assert type(firstname) == str

    lastname = response_data_json["booking"]["lastname"]
    assert lastname == "Brown"

    totalprice = response_data_json["booking"]["totalprice"]
    assert totalprice == 111

    depositpaid = response_data_json["booking"]["depositpaid"]
    assert depositpaid == True

    checkin = response_data_json["booking"]["bookingdates"]["checkin"]
    print("checkin date = ", checkin)
    assert checkin == "2018-01-01"

    checkout = response_data_json["booking"]["bookingdates"]["checkout"]
    assert checkout == "2019-01-01"

    # time = response.elapsed.total_seconds()
    # assert time < 3

@allure.title("TC#2 - Create Booking CRUD Negative")
@allure.description("Verify that invalid payload Booking is not created!")
@pytest.mark.crud
def test_create_booking_negative_tc1():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    json_payload = {}
    response = requests.post(url=URL, headers=headers, json=json_payload)
    assert response.status_code == 500
    assert response.text == "Internal Server Error"






    # https: // jsonpathfinder.com
    # x.booking.bookingdates.checkin
    # response_data_json["booking"]["bookingdates"]["checkin"]




