# Amanda Wedergren
# April 24, 2025
# Module 9.2 Assignment

import requests
import json

response = requests.get("https://anapioficeandfire.com/api/houses/1")
print(response.status_code)
print(response.json())


# create a formatted string of the Python JSON object
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())