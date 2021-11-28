from json import loads
from config.info import Config

class JsonParser():
    ''' for import  config variable for json to python objects  '''
    def __init__(self,dir):
        super().__init__()
        self.dir=dir

    def parse(self): return Config()