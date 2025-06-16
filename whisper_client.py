import requests
import os


# SERVER_URL = "http://192.168.1.3:5000/transcribe"
SERVER_URL = "http://10.5.0.2:5000/transcribe"
# SERVER_URL = "http://localhost:5000/transcribe"


def send_audio_for_transcription(audio_file_path):
    """
    Sends an audio file to the transcription server and prints the response.
    """
    if not os.path.exists(audio_file_path):
        print(f"Error: Audio file not found at {audio_file_path}")
        return

    try:
        with open(audio_file_path, 'rb') as audio_file:
            files = {'audio': (os.path.basename(audio_file_path), audio_file, 'audio/wav')}
            print(f"Sending audio file '{audio_file_path}' to {SERVER_URL}...")
            response = requests.post(SERVER_URL, files=files)

            if response.status_code == 200:
                transcription = response.json().get("transcription")
                print("\nTranscription received:")
                print(transcription)
            else:
                print(f"Error from server: {response.status_code}")
                print(response.json().get("error", "No error message provided."))
    except requests.exceptions.ConnectionError:
        print(f"Connection Error: Could not connect to the server at {SERVER_URL}")
        print("Please ensure the server is running on your computer and the IP address is correct.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == '__main__':
    # Replace 'path/to/your/audio.wav' with the actual path to an audio file on your robot.
    # Your robot will need a way to record and save these audio files.
    # For testing, you can use a dummy file.
    test_audio_file = "data/audio_test.mp4"
    send_audio_for_transcription(test_audio_file)
