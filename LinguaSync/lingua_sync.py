#!/usr/bin/env python3

import requests

RAPIDAPI_KEY = "3411873728mshf212de1e4166200p1be88ejsn1d9778ef5dea"

def get_supported_languages():
    url = "https://google-translate113.p.rapidapi.com/api/v1/translator/support-languages"
    headers = {
        "X-RapidAPI-Host": "google-translate113.p.rapidapi.com",
        "X-RapidAPI-Key": RAPIDAPI_KEY,
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    if response.status_code == 200:
        return data if isinstance(data, list) else []  # Assuming languages are directly in the 'data' list
    else:
        print("Failed to fetch supported languages. Status code: {}".format(response.status_code))
        print("Error message: {}".format(data.get('message', 'Unknown error')))
        return []

def detect_language(RAPIDAPI_KEY, text):
    url = "https://google-translate113.p.rapidapi.com/api/v1/translator/detect-language"
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": "google-translate113.p.rapidapi.com"
    }
    payload = {"text": text}

    response = requests.post(url, data=payload, headers=headers)
    data = response.json()

    if response.status_code == 200:
        detected_language = data.get('language', 'N/A')
        print("Detected Language: {}".format(detected_language))
        return detected_language
    else:
        print("Failed to detect language. Status code: {}".format(response.status_code))
        print("Error message: {}".format(data.get('message', 'Unknown error')))
        return None

def translate_text(api_key, from_lang, to_lang, text):
    url = "https://google-translate113.p.rapidapi.com/api/v1/translator/text"
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "google-translate113.p.rapidapi.com"
    }
    payload = {"from": from_lang, "to": to_lang, "text": text}

    response = requests.post(url, data=payload, headers=headers)
    data = response.json()

    if response.status_code == 200:
        translated_text = data.get('data', {}).get('translation', 'N/A')
        print("Original Text: {}".format(text))
        print("Translated Text: {}".format(translated_text))
    else:
        print("Failed to translate text. Status code: {}".format(response.status_code))
        print("Error message: {}".format(data.get('message', 'Unknown error')))

if __name__ == "__main__":
    print("Welcome to LinguaSync - Your Command Line Language Tool!")

    # Get the list of supported languages
    supported_languages = get_supported_languages()

    if supported_languages:
        print("Here is a list of our Supported Languages:")
        for lang_info in supported_languages:
            language_code = lang_info.get('language_code', 'N/A')
            language_name = lang_info.get('language_name', 'N/A')
            print("{}: {}".format(language_code, language_name))

        text_to_translate = input("Enter your text for translation: ")

        # Detect the language
        detected_language = detect_language(RAPIDAPI_KEY, text_to_translate)

        if detected_language:
            target_language = input("Enter the target language code from the list above: ")

            if any(lang_info.get('language_code') == target_language for lang_info in supported_languages):
                # Translate the text
                translate_text(RAPIDAPI_KEY, detected_language, target_language, text_to_translate)
            else:
                print("Invalid language code. Please enter a valid language code from the list.")
    else:
        print("Exiting due to an error fetching supported languages.")
