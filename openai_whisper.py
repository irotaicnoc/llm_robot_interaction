audio_file_path = 'data/audio_test.mp4'

# import httpx
#
#
# with open(audio_file_path, 'rb') as f:
#     files = {'file': ('audio_test.mp4', f)}
#     response = httpx.post(url='http://localhost:8000/v1/audio/transcriptions', files=files)
#
# print('------------------------------------------')
# print(response)
# print('------------------------------------------')
# print(response.text)
# print('------------------------------------------')

# ======================================================================================================================

# import requests
#
#
# url = 'http://localhost:8000/v1/audio/transcriptions'
# with open(audio_file_path, 'rb') as f:
#     files = {'file': ('audio_test.mp4', f)}
#     # Send the POST request
#     response = requests.post(url=url, data=files, headers={'Content-Type': 'application/binary'})

# ======================================================================================================================

# from pathlib import Path
# from openai import OpenAI
#
# client = OpenAI(api_key='whatever', base_url='http://localhost:8000/v1')
#
# with Path(audio_file_path).open('rb') as audio_file:
#     # transcription = client.audio.transcriptions.create(model='Systran/faster-distil-whisper-small.en', file=audio_file)
#     transcription = client.audio.transcriptions.create(model='Systran/faster-whisper-small', file=audio_file)
#
# print(transcription.text)

# ======================================================================================================================

import requests


url = 'http://localhost:8000/v1/models'
response = requests.post(url=url, data='Systran/faster-whisper-small', headers={'Content-Type': 'application/json'})
print(response)

# ======================================================================================================================