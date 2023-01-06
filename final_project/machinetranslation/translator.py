"""Class for translating en-fr and fr-en."""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']

AUTHENTICATOR = IAMAuthenticator(APIKEY)
LANGUAGE_TRANSLATOR = LanguageTranslatorV3(version='2018-05-01', authenticator=AUTHENTICATOR)
LANGUAGE_TRANSLATOR.set_service_url(URL)

def english_to_french(english_text):
    """English to French."""
    french_text = LANGUAGE_TRANSLATOR.translate(
        text=english_text,
        model_id='en-fr').get_result()["translations"][0]["translation"]
    return french_text

def french_to_english(french_text):
    """French to English."""
    english_text = LANGUAGE_TRANSLATOR.translate(
        text=french_text,
        model_id='fr-en').get_result()["translations"][0]["translation"]
    return english_text
