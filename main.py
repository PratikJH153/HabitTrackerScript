import requests
import datetime as dt

USERNAME = "pratikjh"
TOKEN = "jlskadjflkasjdfasdf"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(pixela_endpoint, json=user_params)
# response.raise_for_status()
# print(response.text)

header = {
    "X-USER-TOKEN": TOKEN
}


def create_graph():
    graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

    graph_config = {
        "id": "graph1",
        "name": "Coding Graph",
        "unit": "Hrs",
        "type": "float",
        "color": "sora"
    }

    response = requests.post(graph_endpoint, json=graph_config, headers=header)
    response.raise_for_status()
    print(response.text)


def update_graph():
    graph_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

    graph_params = {
        "color": "ajisai"
    }

    response = requests.put(graph_update_endpoint, json=graph_params, headers=header)
    response.raise_for_status()
    print(response.text)


def create_pixel():
    pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

    today = dt.datetime(year=2022, month=1, day=26)
    today = today.strftime("%Y%m%d")

    print(today)

    pixel_params = {
        "date": today,
        "quantity": "8"
    }

    response = requests.post(pixel_endpoint, json=pixel_params, headers=header)
    response.raise_for_status()
    print(response.text)


def update_pixel():
    today = dt.datetime.now()
    today = today.strftime("%Y%m%d")

    print(today)

    pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today}"

    pixel_params = {
        "quantity": "5"
    }

    header = {
        "X-USER-TOKEN": TOKEN
    }

    response = requests.put(pixel_update_endpoint, json=pixel_params, headers=header)
    response.raise_for_status()
    print(response.text)