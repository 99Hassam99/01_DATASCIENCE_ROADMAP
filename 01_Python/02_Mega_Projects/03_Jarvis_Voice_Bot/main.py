# sr is a short-form of speechrecognition now we can use sr in our code instead of speech_recognition
from http.client import responses

import speech_recognition as sr
import webbrowser
import pyttsx3
import music_library
import requests
# import os
# from gtts import gTTS
# import pygame


recognizer = sr.Recognizer()
engine = pyttsx3.init()
# newsapi = os.getenv("NEWS_API_KEY")
# huggingface_api_key = os.getenv("HUGGINGFACE_API_KEY")
newsapi = "8df56b454b1d42d7ad3bb3c467bfe53f"
url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}"

def speak(text):
    engine.say(text)
    engine.runAndWait()

# def speak(text):
#     tts =gTTS(text)
#     tts.save("temp.mps")
#     pygame.mixer.init()
#     pygame.mixer.music.load('temp.mp3')
#     pygame.mixer.music.play()
#     while pygame.mixer.music.get_busy():
#         pygame.time.Clock().tick(10)


def aiProcess(command):
    API_KEY = "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"
    API_URL = "https://api-inference.huggingface.co/models/gpt2"

    # The headers with your API key
    headers = {"Authorization": f"Bearer {API_KEY}"}

    # Function to send a prompt to the Hugging Face API
    def query_huggingface_api(prompt):
        response = requests.post(API_URL, headers=headers, json={"inputs": prompt})

        # Check if the response is successful
        if response.status_code == 200:
            output = response.json()

            # Access the generated text from the response
            if isinstance(output, list) and len(output) > 0:
                return output[0]['generated_text']
            else:
                return "Unexpected response format or empty response."

            #     return output[0]['generated_text']
            # else:
            #     return "Unexpected response format or empty response."
        else:
            return f"Error: {response.status_code}, {response.text}"
    return query_huggingface_api(f'virtual assistantJarvis: {command}')
    # command = ""  # Replace this with your user command
    # generated_response = query_huggingface_api(
    #     f"You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please. {command}")

    # print(generated_response)


def processCommand(c):
    # print(f'processing command: {c}')
    # command_lower =c.lower().strip()
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        if song in music_library.music:
            link = music_library.music[song]
            webbrowser.open(link)
            speak(f'playing: {song}')
        else:
            speak("song not found.")
    elif "tell me the news" in c.lower():
        url = (f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        r =requests.get(url)
        print(f'API Response: {r.status_code}, {r.text}')
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            # Extract the articles
            articles = data.get("articles",[])
            # Print the headlines
            for article in articles:
                speak(article['title'])
        else:
            speak("failed to retrieve news.")
    else:
        speak(" let's OpenAi handle the request")
        output = aiProcess(c)
        speak(output)



if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # listen for the word Jarvis
        # obtain audio from the microphone
        r = sr.Recognizer()
        # recognize speech using Sphinx
        print("recognizing....")
        try:
            with sr.Microphone() as source:
                print("Listening...!")
                audio = r.listen(source)
            word = r.recognize_google(audio)
            if(word.lower()== "jarvis"):
                speak("Ya")
                # listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...!")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print(f'Recognized command: {command}')

                    processCommand(command)

        except sr.WaitTimeoutError:
            print("Listening timed out, please try again!")
        except Exception as e:
            print("Error; {0}".format(e))