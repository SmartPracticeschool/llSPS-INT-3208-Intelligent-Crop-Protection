from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from playsound import playsound

authenticator = IAMAuthenticator('fumBqyCTaCbMHNOsJDHaFn2eIkGDO2P9UbEiAIFd1HLE')
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url('https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/13787e5d-dfd8-4822-92e2-f657bd5e2ba2')

with open('Hello_world.mp3', 'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            'Hello how r u',
            voice='en-US_AllisonV3Voice',
            accept='audio/mp3'        
        ).get_result().content)
playsound('Hello_world.mp3')    
