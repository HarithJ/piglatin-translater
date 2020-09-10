import requests
import os

print("\n\n")
print("  Welcome To English To Pig Latin Translator  ")
print("----------------------------------------------")
print("\n")

engText = input("Please enter English text: ")
print("\n")

url = os.getenv(TRANS_URL, 'http://127.0.0.1:5000/translate')
engTextObject = {'engText': engText}

response = requests.post(url, json = engTextObject)
parsedResponse = response.json()

translation = parsedResponse["translation"]

print(f"Pig Latin Translation: {translation}")
print("\n")