from requests import get

GET_DEFINITION = 'https://api.dictionaryapi.dev/api/v2/entries/{0}/{1}'

class Dictionary:
    def __init__(self, lang='en'):
        self.lang = lang

    def get_definitions_for(self, term):
        url = GET_DEFINITION.format(self.lang, term)
        return get(url).json()