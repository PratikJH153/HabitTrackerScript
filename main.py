import requests

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "jlskadjflkasjdfasdf",
    "username": "pratikjh",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(pixela_endpoint, json=user_params)
response.raise_for_status()
print(response.text)
