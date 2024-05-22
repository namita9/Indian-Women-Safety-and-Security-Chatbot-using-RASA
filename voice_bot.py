import requests
import speech_recognition as sr
import pyttsx3

# Function to speak text
def speak(text):
    engine = pyttsx3.init()
    indian_female_voice = None
    voices = engine.getProperty('voices')
    for voice in voices:
        if "female" in voice.name.lower() and ("india" in voice.languages[0].lower() or "hindi" in voice.languages[0].lower()):
            indian_female_voice = voice
            break
    if indian_female_voice:
        engine.setProperty('voice', indian_female_voice.id)
    engine.say(text)
    engine.runAndWait()

# Function to send message to Rasa server and receive response
def send_message(message):
    r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": message})
    bot_message = ""
    for i in r.json():
        bot_message = i['text']
    return bot_message

# Initial interaction with the bot
print("Bot says:")
bot_message = send_message("Hello")
print(bot_message)
speak(bot_message)

# Interaction loop
while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything:")
        audio = r.listen(source)
        try:
            message = r.recognize_google(audio)
            print("You said : {}".format(message))
        except:
            print("Sorry could not recognize your voice")
            continue

    if len(message) == 0:
        continue

    # Sending message to Rasa server
    bot_message = send_message(message)
    print("Bot says:", bot_message)

    # Speaking bot's response
    speak(bot_message)

    # End conversation if "goodbye" is said
    if message.lower() == "goodbye":
        print("Goodbye!")
        break
