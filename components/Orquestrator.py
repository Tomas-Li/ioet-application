"""
Module in charge of:
    -Reading the config file
    -Defining the order of execution of all the function
"""

#Built-in imports
import configparser


#Constants



#Local Classes
from .Containers.ContainerInterface import ContainerInterface
from .Containers.ContainerPayments import ContainerPayment
from .Containers.ContainerEmployees import ContainerEmployees

class Orquestrator():
    def __init__(self):
        #ConfigFile
        config = configparser.ConfigParser()
        config.read('./configFile.ini')

        PATHPAYMENTS = config["PATHS"]["PATHPAYMENTS"].replace("'", '')
        PATHEMPLOYEES = config["PATHS"]["PATHEMPLOYEES"].replace("'", '')

        #Instantiation
        self.containerPayments = ContainerPayment();
        self.containerEmployees = ContainerEmployees([]);

        #Data load
        self.containerLoader(self.containerPayments, PATHPAYMENTS)
        self.containerLoader(self.containerEmployees, PATHEMPLOYEES)

    
    @staticmethod
    def containerLoader(container: ContainerInterface, path: str):
        container.load(path)

    def execute(self):
        pass