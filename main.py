# pip install pyttsx3

import pyttsx3

text_speech = pyttsx3.init()
while True:
      answer = input("Write what you want me to speak : ")
      if answer == "q":
          break
      text_speech.say(answer)
      text_speech.runAndWait()