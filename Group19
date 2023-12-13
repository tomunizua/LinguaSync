#!/usr/bin/python3
import requests

# These are the RAPID API credentials
rapidapi_host = "google-translate1.p.rapidapi.com"
rapidapi_key = "f6b0cedb0dmsh37e00174a4d5e60p11b68cjsndb0a3f5d2356"

# Function to translate text
def translate_text(text, source_language, target_language):
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

    headers = {
	"content-type": "application/x-www-form-urlencoded",
	"Accept-Encoding": "application/gzip",
	"X-RapidAPI-Key": "f6b0cedb0dmsh37e00174a4d5e60p11b68cjsndb0a3f5d2356",
	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }

    data = {
        "q": text.encode('utf-8'),
        "source": source_language,
        "target": target_language,
    }

    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()

    translation = response.json()["data"]["translations"][0]

    return translation["translatedText"]

def main():
    # Instructions on how to use our translator
    print("Welcome to Group 19 Translate Tool! This tool allows you to translate text between different languages.")
    print("Short tutorial in steps, here's how to use it:")
    print("Step 1 - Enter the source language code (e.g., en for English, fr for French).")
    print("Step 2 - Enter the target language code (e.g., es for Spanish, de for German).")
    print("Step 3 - Enter the text you want to translate.")
    print("Step 4 - TA-DA... Our translator tool will then display the translated text.\n")
    print("Let's Go!!!\n")

    # Display to use the translator
    source_language = input("Enter the source language code (e.g., en, fr): ").strip()
    target_language = input("Enter the target language code (e.g., es, de): ").strip()
    text_to_translate = input("Enter the text to translate: ").strip()

    # Translate the text
    translated_text = translate_text(text_to_translate, source_language, target_language)

    # Print the translated text
    print("Translated text:")
    print(translated_text)

if __name__ == "__main__":
    main()
