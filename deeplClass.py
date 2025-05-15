import deepl 
from dotenv import load_dotenv
import os

load_dotenv()

class DeeplClass:
 
    def __init__(self):
        api_key = os.getenv("DEEPL_API_KEY")
        if not api_key:
            raise ValueError("DEEPL_API_KEY n'a pas ete trouver")
        self.translator = deepl.Translator(api_key)
    
    def retrieve_language(self):
        langage = self.translator.get_source_languages()
        ret_lang = []
        for j in langage:
            ret_lang.append({ "code": j.code, "name" : j.name}) 
        return ret_lang
    
    def translate_language(self, text, lang):
        try:
            result= self.translator.translate_text(text, target_lang=f"{lang}")
            return result.text
        except Exception as e:
            raise RuntimeError(f"Translation failed: {e}")
    



