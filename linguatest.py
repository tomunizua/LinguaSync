import requests

API_KEY = '3411873728mshf212de1e4166200p1be88ejsn1d9778ef5dea'
BASE_URL = 'https://abit-translator.p.rapidapi.com/translate'

def get_supported_languages():
    url = BASE_URL + '/languages'
    headers = {
        'X-RapidAPI-Key': API_KEY,
        'Content-Type': 'application/json',
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching supported languages: {response.text}")
        return None

def detect_language(text):
    url = BASE_URL + '/detect'
    headers = {
        'X-RapidAPI-Key': API_KEY,
        'Content-Type': 'application/json',
    }
    data = {
        'q': text
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()['language']
    else:
        print(f"Error detecting language: {response.text}")
        return None

def translate_text(text, target_lang_code):
    url = BASE_URL + '/translate'
    headers = {
        'X-RapidAPI-Key': API_KEY,
        'Content-Type': 'application/json',
    }
    data = {
        'q': text,
        'target': target_lang_code
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()['translatedText']
    else:
        print(f"Error translating text: {response.text}")
        return None

# Example usage
supported_languages = get_supported_languages()
if supported_languages:
    print("Supported Languages:")
    for lang_info in supported_languages:
        lang_code = lang_info['code']
        lang_name = lang_info['language']
        print(f"{lang_code}: {lang_name}")

    text_to_translate = input("Enter your text for translation: ")
    detected_language = detect_language(text_to_translate)

    if detected_language:
        print(f"Detected language: {detected_language}")

        target_lang_code = input("Enter the target language code from the list above: ")
        translation = translate_text(text_to_translate, target_lang_code)

        if translation:
            print(f"Translation: {translation}")
