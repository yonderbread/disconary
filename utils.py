import json
class Config:
    def __init__(self, filename='config.json'):
        self.filename = filename
        self.contents = None

    def load(self):
        try:
            with open(self.filename, 'r') as config_file:
                file_contents = config_file.read()
                parsed_contents = json.loads(file_contents)
                self.contents = parsed_contents
                return self.contents
        except FileNotFoundError:
            return False

    def save(self):
        try:
            with open(self.filename,'w') as config_file:
                json.dump(self.contents, config_file)
                return True
        except FileNotFoundError:
            return False