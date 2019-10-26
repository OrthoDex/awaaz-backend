# Imports the Google Cloud client library
GOOGLE_APPLICATION_CREDENTIALS='./calhacks6-0da77a79a6ba.json'
IMPEDIMENT_FILE='./ounces-litre.wav'
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

# Instantiates a client
client = speech.SpeechClient.from_service_account_json(filename=GOOGLE_APPLICATION_CREDENTIALS)

# The name of the audio file to transcribe
file_name = IMPEDIMENT_FILE

# Loads the audio into memory
with io.open(file_name, 'rb') as audio_file:
    content = audio_file.read()
    audio = types.RecognitionAudio(content=content)

config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code='en-US')

# Detects speech in the audio file
response = client.recognize(config, audio)

transcript = ""
for result in response.results:
    transcript=result.alternatives[0].transcript
    print('Transcript: {}'.format(result.alternatives[0].transcript))
