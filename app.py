#!/usr/bin/env python3

import requests

url = 'https://mtzdkn64d7.execute-api.eu-north-1.amazonaws.com/default/GetScoringBoard'

# Request payload (if required)
payload = {
    'name': 'jojo'
}

# Optional headers (if required)
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer your_token'
}

# Send the POST request
response_1 = requests.post(url, json=payload, headers=headers)
response_2 = requests.get(url, json=payload, headers=headers)

# Print the response
print(response_1.status_code)  # HTTP status code
print(response_1.text)  # Response body

print(response_2.status_code)  # HTTP status code
print(response_2.text)  # Response body


