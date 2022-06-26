"""
Module in charge of orchestrating the program. 
This code will execute the following order of actions:
    -Read the config file and keep its values.
    -Instantiate the classes.
    -Read the data (payments and employees) from the indicated files.
    -Calculate the total payments of all employees
    -Output the results

Methods:
-------
    configFileReading(self)
    containerLoader(container: ContainerInterface, path: str)
    execute(self)
"""

#Built-in imports
import configparser

#Local Classes
from .Containers.ContainerInterface import ContainerInterface
from .Containers.ContainerPayments import ContainerPayment
from .Containers.ContainerEmployees import ContainerEmployees
from .Writer import Writer

#Local functions
from ..util.calculation import calculation


class Orquestrator():
    """
    Module in charge of orchestrating the program. 
    This class will execute the following order of actions:
        -Read the config file and keep its values.
        -Instantiate the classes.
        -Read the data (payments and employees) from the indicated files.
        -Calculate the total payments of all employees
        -Output the results

    Methods:
    -------
    configFileReading(self):
        Method for loading all the configuration variables from configFile.ini

    containerLoader(container: ContainerInterface, path: str):
        Method that calls the load method from implementations of the interface ContainerInterface

    execute(self):
        Main method of the class. Is the one that makes the calls to load the containers, calculate the payments, and output the data
    """

    def __init__(self, configPath='./configFile.ini') -> None:
        """
        Will call configFileReading to read the configuration file, and will isntantiate both container classes

        Parameters:
        ----------
        configPath : string ; defaultValue
            This is the path to the configurationFile to use. It's given as a parameter in case of having more than one config file, and for testing purposes
        """

        #ConfigFile
        self.configPath = configPath
        self.configFileReading();

        #Instantiation
        self._containerPayments = ContainerPayment();
        self._containerEmployees = ContainerEmployees();


    @staticmethod
    def containerLoader(container: ContainerInterface, path: str) -> None:
        """
        Method that calls the load method from implementantions of the interface ContainerInterface
        """
        container.load(path)


    def configFileReading(self) -> None:
        """
        Method for loading all the configuration variables from configFile.ini
        """

        config = configparser.ConfigParser()
        config.read(self.configPath)

        self._configVariables = {}

        #PATHS
        self._configVariables["PATHPAYMENTS"] = config["PATHS"]["PATHPAYMENTS"].replace("'", '')
        self._configVariables["PATHEMPLOYEES"] = config["PATHS"]["PATHEMPLOYEES"].replace("'", '')
        self._configVariables["PATHOUTPUT"] = config["PATHS"]["PATHOUTPUT"].replace("'", '')

        #INPUT
        # not used as there is no currency conversion
        # self._configVariables["INPUT_CURRENCY_PAYMENTS"] = config["INPUT"]["INPUT_CURRENCY_PAYMENTS"].replace("'", '').upper()

        #OUTPUT
        self._configVariables["OUTPUT_TYPE"] = config["OUTPUT"]["OUTPUT_TYPE"].replace("'", '')


    def execute(self) -> str:
        """
        Main method of the class. Is the one that makes the calls to load the containers, calculate the payments, and output the data
        """

        #Data load
        self.containerLoader(self._containerPayments, self._configVariables["PATHPAYMENTS"])
        self.containerLoader(self._containerEmployees, self._configVariables["PATHEMPLOYEES"])

        #Calculation
        results = calculation(self._containerPayments, self._containerEmployees)

        #Output
        writer = Writer(self._configVariables["OUTPUT_TYPE"], self._configVariables["PATHOUTPUT"])
        writer.write(results)

        return writer.fileOutputName()