import deepl 
from dotenv import load_dotenv
import os

load_dotenv()

class DeeplClass:
 
    def __init__(self):
        api_key = os.getenv("DEEPL_API_KEY")
        self.translator = deepl.Translator(api_key)
    
    def retrieve_language(self):
        langage = self.translator.get_source_languages()
        ret_lang = []
        
        for i,j in enumerate(langage):
            ret_lang.append({ "code": j.code, "name" : j.name})
            
        return ret_lang
    
    def translate_language(self, text, lang):
        result= self.translator.translate_text(text, target_lang=f"{lang}")
        return result.text
    



