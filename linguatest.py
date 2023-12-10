#!/usr/bin/env python3

import requests
import json

RAPIDAPI_KEY = "3411873728mshf212de1e4166200p1be88ejsn1d9778ef5dea"

def detect_language(api_key, text):
    url = "https://microsoft-translator-text.p.rapidapi.com/Detect"
    querystring = {"api-version": "3.0"}
    payload = [{"Text": text}]
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "microsoft-translator-text.p.rapidapi.com"
    }
    response = requests.post(url, json=payload, headers=headers, params=querystring)
    detected_language = response.json()[0]['language']
    return detected_language

def get_supported_languages(RAPIDAPI_KEY):
    url = "https://microsoft-translator-text.p.rapidapi.com/languages"
    querystring = {"api-version": "3.0"}
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": "microsoft-translator-text.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    print(response.json())

    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx errors

        supported_languages = response.json()
        return supported_languages

    except requests.exceptions.RequestException as e:
     print(f"Failed to fetch supported languages. Error: {e}")
     print(f"Response content: {response.content.decode('utf-8')}")
    return None



def translate_text(api_key, text, target_language):
    url = "https://microsoft-translator-text.p.rapidapi.com/translate"
    querystring = {"to": target_language, "api-version": "3.0"}
    payload = [{"Text": text}]
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "microsoft-translator-text.p.rapidapi.com"
    }
    response = requests.post(url, json=payload, headers=headers, params=querystring)
    translated_text = response.json()[0]['translations'][0]['text']
    return translated_text

if __name__ == "__main__":
    print("Welcome to LinguaSync - Your Command Line Language Tool!")

    # Detect language
    text_to_translate = input("Enter your text for translation: ")
    detected_language = detect_language(RAPIDAPI_KEY, text_to_translate)
    
    # Fetch the language name using the detected language code
    supported_languages = get_supported_languages(RAPIDAPI_KEY)
    detected_language_name = supported_languages.get(detected_language, "Unknown")

    print(f'Detected Language Code: {detected_language} ({detected_language_name})')

    # Get supported languages
    supported_languages = get_supported_languages(RAPIDAPI_KEY)
    if supported_languages:
        print("Supported Languages:")
    for lang_code, lang_name in supported_languages.items():
        print(f"{lang_code}: {lang_name}")
    else:
        print("No supported languages available.")

    # Translate text
    target_language = input("Enter the target language code from the list above: ")
    if target_language not in supported_languages:
        print("Invalid language code. Please enter a valid language code from the list.")
    else:
        translated_text = translate_text(RAPIDAPI_KEY, text_to_translate, target_language)
        print(f'Translated Text: {translated_text}')

