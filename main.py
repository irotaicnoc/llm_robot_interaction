import requests
import json

# Define the URL for the API endpoint
url = 'http://localhost:11434/api/generate'
# Define the payload (data) to be sent in the request body
payload = {
    'model': 'tinyllama_1b_prompt',
    'prompt': 'what are your tasks?',
    'stream': False
}
# Convert the payload to a JSON string
json_payload = json.dumps(payload)
# Define the headers for the request
headers = {'Content-Type': 'application/json'}

# Send the POST request
response = requests.post(url, data=json_payload, headers=headers)
# Parse the JSON response
response_data = response.json()
# Print the response data
print('Response from API:')
print(json.dumps(response_data, indent=4))

