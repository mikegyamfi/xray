import random
import re
import secrets
import json
import string

import requests
from datetime import datetime
from decouple import config

ishare_map = {
    2: 50,
    4: 52,
    7: 2000,
    10: 3000,
    12: 4000,
    15: 5000,
    18: 6000,
    22: 7000,
    25: 8000,
    30: 10000,
    45: 15000,
    60: 20000,
    75: 25000,
    90: 30000,
    120: 40000,
    145: 50000,
    285: 100000,
    560: 200000
}


def ref_generator(length=8):
    characters = string.ascii_uppercase + string.digits

    # Generate a random sequence of the specified length
    reference = ''.join(random.choice(characters) for _ in range(length))

    return reference


def top_up_ref_generator():
    now_time = datetime.now().strftime('%H%M')
    secret = secrets.token_hex(1)

    return f"TOPUP-{now_time}{secret}".upper()


def send_bundle(receiver, bundle_amount, reference):
    url = "https://controller.geosams.com/api/v1/new_transaction"
    print(receiver, bundle_amount, reference)

    payload = json.dumps({
        "account_number": receiver,
        "reference": reference,
        "bundle_amount": bundle_amount
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': config("BEARER_TOKEN")
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    return response


def value_for_moni_send_bundle(receiver, bundle_amount, reference):
    url = "https://www.value4moni.com/api/v1/inititate_transaction"

    headers = {
        'Content-Type': 'application/json',
    }

    # Create the payload for the POST request
    payload = {
        "API_Key": config("MONI_API_KEY"),
        "Receiver": str(receiver),
        "Volume": str(bundle_amount),
        "Reference": reference,
        "Package_Type": "AirtelTigo"
    }

    # Convert the payload into JSON format
    json_payload = json.dumps(payload)

    # Make the POST request to the API
    response = requests.post(url, headers=headers, data=json_payload)

    print(response.json())
    return response


