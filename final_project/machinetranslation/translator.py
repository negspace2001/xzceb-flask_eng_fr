""" Module for translation using IBM Watson Translator """
import json
import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

apiKey = os.environ['apiKey']
url = os.environ['url']
version = os.environ['version']

authenticator = IAMAuthenticator(apiKey)
language_translator = LanguageTranslatorV3(
    version=version,
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """ Function which translates English Text to French """
    french_translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    #print(json.dumps(french_translation, indent=2, ensure_ascii=False))
    
    french_text = french_translation["translations"][0]["translation"]
    print("Translation: ", english_text, " --> ", french_text)

    return french_text

def french_to_english(french_text):
    """ Function which translates French Text to English """
    english_translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    #print(json.dumps(english_translation, indent=2, ensure_ascii=False))

    english_text = english_translation["translations"][0]["translation"]
    print("Translation: ", french_text, " --> ", english_text)

    return english_text
