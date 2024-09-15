import json

import requests

url = "https://www.value4moni.com/api/v1/inititate_transaction"


headers = {
    'Content-Type': 'application/json',
}

# Create the payload for the POST request
payload = {
    "API_Key": "d789d5a7-c11d-4b99-9e08-0e28aa9a9d3f",
    "Receiver": "0272266444",
    "Volume": "1000",
    "Reference": "gcvhbj76tr54rxrf",
    "Package_Type": "AirtelTigo"
}

# Convert the payload into JSON format
json_payload = json.dumps(payload)

# Make the POST request to the API
response = requests.post(url, headers=headers, data=json_payload)

# Check the status code and response
if response.status_code == 200:
    print("Transaction initiated successfully!")
    print("Response:", response.json())  # Print the JSON response from the API
else:
    print(f"Failed to initiate transaction. Status code: {response.status_code}")
    print("Error message:", response.text)
