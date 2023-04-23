"""This is a translator module"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version = '2023-04-23'

def englishToFrench(english_text):
    """This class does english to french translation"""

    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(version=version, authenticator=authenticator)
    language_translator.set_service_url(url)

    lt = language_translator
    translation = lt.translate(text=english_text, model_id="en-fr").get_result()
    frenchText = translation['translations'][0]['translation']
    return frenchText

def frenchToEnglish(french_text):
    """This class does french to english translation"""

    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(version=version, authenticator=authenticator)
    language_translator.set_service_url(url)

    lt = language_translator
    translation = lt.translate(text=french_text, model_id="fr-en").get_result()
    englishText = translation['translations'][0]['translation']
    return englishText
