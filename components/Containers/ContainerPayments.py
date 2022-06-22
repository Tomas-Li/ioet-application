#Built-in modules
import json

#Local modules
from .ContainerInterface import ContainerInterface

class ContainerPayment(ContainerInterface):
    def __init__(self) -> None:
        """
        Parameters
        ----------
        path : str
            A string with the relative path of the file to read (extension .txt included)
        
        """
        self._container = {};
        self._fileType = '';
        
    
    @property
    def container(self) -> dict:
        return self._container

    def load(self, path: str) -> None:
        self._fileType = str(path.split('.')[-1])
        if(self._fileType == 'json'):
            self.loadFromJson(path)
        else:
            raise Exception("In ContainerPayments: fileType wasn't recognize")


    def loadFromJson(self, path: str) -> None:
        """
        Method for loading payments from a .json file. Path given through configFile.ini
        """
        with open(path, mode='r', encoding='utf-8') as f:
            self._container = json.load(f)