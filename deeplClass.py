import deepl 
import requests

class DeeplClass:
    def __init__(self):
        self.translator = deepl.Translator("e5b8191a-9b27-41de-928b-85e3fd9fd0a1:fx")
    
    def retrieve_language(self):
        langage = self.translator.get_source_languages()
        ret_lang = []
        
        for i,j in enumerate(langage):
            ret_lang.append({ "code": j.code, "name" : j.name})
            
        return ret_lang
    
    def translate_language(self, text, lang):
        result= self.translator.translate_text(text, target_lang=f"{lang}")


