# import requests
#
#
# # command = 'curl http://localhost:11434/api/generate -d \'{"model": "tinyllama_1b_prompt", "prompt": "what are your tasks?", "stream": false}\''
# response = requests.get(
#     'http://localhost:11434/api/generate',
#     params={"model": "tinyllama_1b_prompt", "prompt": "what are your tasks?", "stream": False},
# )
# print('----------------------')
# print('out:')
# print(response.status_code)
# print(response.headers['content-type'])
# print(response.encoding)
# print(response.text)
# print(response.json)
# print('----------------------')


import requests
import json

# Define the URL for the API endpoint
url = "http://localhost:11434/api/generate"

# Define the payload (data) to be sent in the request body
payload = {
    "model": "tinyllama_1b_prompt",
    "prompt": "what are your tasks?",
    "stream": False
}

# Convert the payload to a JSON string
json_payload = json.dumps(payload)

# Define the headers for the request
headers = {
    "Content-Type": "application/json"
}

# Send the POST request
response = requests.post(url, data=json_payload, headers=headers)
print('----------------------')
print('out:')
print(response.status_code)
print(response.headers['content-type'])
print(response.encoding)
print(response.text)
print(response.json)
print('----------------------')
# Parse the JSON response
response_data = response.json()

# Print the response data
print("Response from API:")
print(json.dumps(response_data, indent=4))
print('----------------------')

