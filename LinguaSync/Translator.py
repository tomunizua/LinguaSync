#!/usr/bin/python3

import http.client
import json


LANGUAGE_CODES = {
    'af': 'afrikaans',
    'sq': 'albanian',
    'am': 'amharic',
    'ar': 'arabic',
    'hy': 'armenian',
    'az': 'azerbaijani',
    'eu': 'basque',
    'be': 'belarusian',
    'bn': 'bengali',
    'bs': 'bosnian',
    'bg': 'bulgarian',
    'ca': 'catalan',
    'ceb': 'cebuano',
    'ny': 'chichewa',
    'zh-cn': 'chinese (simplified)',
    'zh-tw': 'chinese (traditional)',
    'co': 'corsican',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'eo': 'esperanto',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'fy': 'frisian',
    'gl': 'galician',
    'ka': 'georgian',
    'de': 'german',
    'el': 'greek',
    'gu': 'gujarati',
    'ht': 'haitian creole',
    'ha': 'hausa',
    'haw': 'hawaiian',
    'iw': 'hebrew',
    'he': 'hebrew',
    'hi': 'hindi',
    'hmn': 'hmong',
    'hu': 'hungarian',
    'is': 'icelandic',
    'ig': 'igbo',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'jw': 'javanese',
    'kn': 'kannada',
    'kk': 'kazakh',
    'km': 'khmer',
    'ko': 'korean',
    'ku': 'kurdish (kurmanji)',
    'ky': 'kyrgyz',
    'lo': 'lao',
    'la': 'latin',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'lb': 'luxembourgish',
    'mk': 'macedonian',
    'mg': 'malagasy',
    'ms': 'malay',
    'ml': 'malayalam',
    'mt': 'maltese',
    'mi': 'maori',
    'mr': 'marathi',
    'mn': 'mongolian',
    'my': 'myanmar (burmese)',
    'ne': 'nepali',
    'no': 'norwegian',
    'or': 'odia',
    'ps': 'pashto',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'pa': 'punjabi',
    'ro': 'romanian',
    'ru': 'russian',
    'sm': 'samoan',
    'gd': 'scots gaelic',
    'sr': 'serbian',
    'st': 'sesotho',
    'sn': 'shona',
    'sd': 'sindhi',
    'si': 'sinhala',
    'sk': 'slovak',
    'sl': 'slovenian',
    'so': 'somali',
    'es': 'spanish',
    'su': 'sundanese',
    'sw': 'swahili',
    'sv': 'swedish',
    'tg': 'tajik',
    'ta': 'tamil',
    'te': 'telugu',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'ur': 'urdu',
    'ug': 'uyghur',
    'uz': 'uzbek',
    'vi': 'vietnamese',
    'cy': 'welsh',
    'xh': 'xhosa',
    'yi': 'yiddish',
    'yo': 'yoruba',
    'zu': 'zulu',
}

def translate_text(source_text, source_lang, target_lang):
    conn = http.client.HTTPSConnection("google-translate1.p.rapidapi.com")

    payload = "text={}&to_lang={}&from_lang={}".format(
        source_text, target_lang, source_lang
    ).encode('utf-8')

    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'Accept-Encoding': "application/gzip",
        'X-RapidAPI-Key': "f6b0cedb0dmsh37e00174a4d5e60p11b68cjsndb0a3f5d2356",
        'X-RapidAPI-Host': "google-translate1.p.rapidapi.com"
    }

    try:
        conn.request("POST", "/language/translate/v2", payload, headers)
        res = conn.getresponse()
        data = res.read().decode("utf-8")

        # Print the raw response for debugging
        print(data)

        response_json = json.loads(data)

        translated_text = None
        if "translations" in response_json:
            translated_text = response_json["translations"][0]["translatedText"]

        return translated_text if translated_text else "Translation error occurred."

    except Exception as e:
        print("Error: {}".format(e))
        return "Translation error occurred."


def display_language_codes():
    print("\nSupported Language Codes:")
    print("------------------------")
    for code, name in LANGUAGE_CODES.items():
        print("{}: {}".format(code, name))

def main():
    print("Welcome to Group19's Language Translation Tool!")
    print("Enter 'langs' to view the list of language codes.")

    source_lang = input("Enter the source language code (e.g., 'en' for English): ")
    if source_lang.lower() == 'langs':
        display_language_codes()
        source_lang = input("\nEnter the source language code: ")

    source_text = input("Enter the text to translate: ")
    target_lang = input("Enter the target language code (e.g., 'es' for Spanish): ")

    translated_text = translate_text(source_text, source_lang, target_lang)

    print("\nTranslation Result:")
    print("-------------------")
    print("Source Text: {}".format(source_text))
    print("Translated Text: {}".format(translated_text.encode('utf-8').decode('unicode-escape')))

if __name__ == "__main__":
    main()

