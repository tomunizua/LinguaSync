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
        return data['data']['languages']
    else:
        print(f"Failed to fetch supported languages. Status code: {response.status_code}")
        print(f"Error message: {data['error']['message']}")
        return []

def detect_language(api_key, text):
    url = "https://google-translate113.p.rapidapi.com/api/v1/translator/detect-language"
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "google-translate113.p.rapidapi.com"
    }
    payload = {"text": text}

    response = requests.post(url, data=payload, headers=headers)
    data = response.json()

    if response.status_code == 200:
        detected_language = data['language']
        print(f"Detected Language: {detected_language}")
        return detected_language
    else:
        print(f"Failed to detect language. Status code: {response.status_code}")
        print(f"Error message: {data['message']}")
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
        translated_text = data['data']['translation']
        print(f"Original Text: {text}")
        print(f"Translated Text: {translated_text}")
    else:
        print(f"Failed to translate text. Status code: {response.status_code}")
        print(f"Error message: {data['message']}")

if __name__ == "__main__":
    print("Welcome to LinguaSync - Your Command Line Language Tool!")

    # Get the list of supported languages
    supported_languages = get_supported_languages()

    if supported_languages:
        print("Supported Languages:")
        for lang_code, lang_name in supported_languages.items():
            print(f"{lang_code}: {lang_name}")

        text_to_translate = input("Enter the text: ")

        # Detect the language
        detected_language = detect_language(RAPIDAPI_KEY, text_to_translate)

        if detected_language:
            target_language = input("Enter the target language code from the list above: ")

            if target_language in supported_languages:
                # Translate the text
                translate_text(RAPIDAPI_KEY, detected_language, target_language, text_to_translate)
            else:
                print("Invalid language code. Please enter a valid language code from the list.")
    else:
        print("Exiting due to an error fetching supported languages.")
