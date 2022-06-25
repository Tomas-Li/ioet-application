"""
ContainerPayments.py
--------------------

This file defines the class ContainerPayments, class in charge of reading and storing all the payments associated data

Attributes:
---------
container

fileType


Methods:
------
load(self, path: str)

loadFromJson(self, path: str)

"""

#Constants
from ...const.consts import WEEKDAYS, BASECONTAINER

#Built-in modules
import json

#Local modules
from .ContainerInterface import ContainerInterface

class ContainerPayment(ContainerInterface):
    """
    This class defines its main container as a dict in which every day is a key and theirs values are the intervals-payments-currencies
    All the data is loaded through the load method, which calls the correct method implementation for reading based on the file extension of the file to read (only json for payments)

    Attributes:
    ----------
    container : dict
        Main container of the class. All the payment data is stored here

    Methods:
    --------
    load(self, path):
        This metod calls the correct method to read a file and fill the container attribute

    loadFromJson(self, path: str):
        Method for loading data from a .json file, path given through configFile.ini

    """

    def __init__(self) -> None:
        """
        Starts the class attributes container=BASECONTAINER and filetype=''
        BASECONTAINER is a imported constant. Is a dictionary with the following structure {"MO": {}, "TU": {}, ...} covering every day of the week

        """

        self._container = BASECONTAINER;
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
        The data will be parsed individually for each hour (the reason for this is explained in docs/propuestas.txt)
        
        Parameters
        ----------
        path : str
            A string for the path with the file to read (extension .json included)
        
        """
        try:
            with open(path, mode='r', encoding='utf-8') as f:
                intervals = json.load(f, parse_int=int)
        except(FileNotFoundError):
            print("A payment.json data file couldn't be found at the input path, please check your configFile->PATHPAYMENTS variable")
            exit()
        
        for day in WEEKDAYS:
            for interval in intervals[day]:
                if interval[0] < interval[1]:
                    for hour in list(range(interval[0], interval[1])):
                        self._container[day][hour] = interval[2];
                else:
                    #That 24 magic number just below si the maximum number of hours in a day,  it didn't make sense to add datetime or to even create a variable for that
                    for hour in (list(range(interval[0], 24)) + list(range(0, interval[1]))):
                        self._container[day][hour] = interval[2];
        
                