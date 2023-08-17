import requests
import json
import pyttsx3

speech = pyttsx3.init()

#set the voice speed
rate = 120
speech.setProperty('rate',rate)

#set the voice
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
speech.setProperty('voice',voice_id)

city = input("Enter the name of the city: ")

#set the API which i take from the weatherapi.com
url = f"https://api.weatherapi.com/v1/current.json?key=a1f7054d71b043feb02101710232107&q={city}"
r = requests.get(url)

weather_dic = json.loads(r.text)
weather_dic2 = json.loads(r.text)

#print the token which i need to print
w1 = weather_dic["current"]["temp_c"]
w2 = weather_dic["current"]["condition"]["text"]

print(f"The current weather in {city} is {w1}\u00b0 celcis and the current situation is {w2}")

speech.say(f"The current weather in {city} is {w1}\u00b0 celcis and the current situation is {w2}")
speech.runAndWait()