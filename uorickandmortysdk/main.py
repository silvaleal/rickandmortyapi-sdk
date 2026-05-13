import requests

class UORickAndMortySDK:
    def __init__(self):
        self.baseUrl = 'https://rickandmortyapi.com/api'
        self.prefix = None # A API é dividida entre tipos de consultar, character, location e episode, o prefixo ajuda a identificar o tipo.
    
    def setPrefix(self, prefix):
        validPrefix = ['character', 'location', 'episode']
        
        if not prefix in validPrefix:
            raise Exception(f"Invalid prefix. Valids: "+ ", ".join(validPrefix)+".")
        
        self.prefix = prefix
        return self
         
    def get(self, id=None, page=1):
        
        finalUrl = f"{self.baseUrl}/{self.prefix}/{id}?page={page}" if id else f"{self.baseUrl}/{self.prefix}?page={page}"
                
        requi = requests.get(finalUrl)
        
        return {
            'status': requi.status_code,
            'result': requi.json()
        }