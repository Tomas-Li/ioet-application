"""
Writer.py
--------

This file defines the class Writer which is in charge of the output of the results

Methods:
-------
    write(self, results: list)
    writeTxt(self, results: list)
    writeJson(self, results: list)
    jsonFormat(self, results: list)
    fileOutputName(self)

"""

from datetime import datetime
import json

class Writer():
    """
    Class in charge of the output of the results
    It will decided the output that will be used based on the config file instructions
    """

    def __init__(self, format: str, path: str) -> None:
        """
        Parameters
        ----------
        format : str
            A string with the format type of the file to write. It's values can be txt | json | console

        path : str
            A string with the relative directory to write the output in.
        """

        timeNow = datetime.now()
        dt_string = timeNow.strftime("%d-%m-%Y-%Hh-%Mm-%Ss")

        self._format = format.lower()
        self._path = f"{path}/{dt_string}.{self._format}"


    def write(self, results: list) -> None :
        """
        Method that redirects to the correct writing function based on the specified format.
        The name of the output file will be the DateTime in which the file is being writen

        Parameters
        ----------
        results : dict
            A dictionary with the calculated results
        """

        if (self._format == 'txt'):
            self.writeTxt(results)
        elif (self._format == 'json'):
            self.writeJson(results)
        elif (self._format == 'console'):
            self.writeConsole(results)
        else:
            print("The output format wasn't a valid option.")
            print("Proceding to generate a .txt file in the output directory")
            self.writeTxt(results)

    
    def writeTxt(self, results: list) -> None:
        """
        Method for writing a txt file with the results

        Parameters
        ----------
        results : dict
            A dictionary with the calculated results
        """

        with open(self._path, mode='w', encoding="utf-8") as f:
            for result in results:
                f.write(f"{result}\n")


    def writeJson(self, results: list) -> None:
        """
        Method for writing a json file with the results

        Parameters
        ----------
        results : dict
            A dictionary with the calculated results
        """

        jsonFormatedResults = self.jsonFormat(results)
        with open(self._path, mode="w", encoding="utf-8") as f:
            json.dump(jsonFormatedResults, f, ensure_ascii=False, sort_keys=True, indent=4)


    def writeConsole(self, results: list) -> list:
        """
        Method for printing on console the results.
        Returns the results as a way of testing all the prosses until this point

        Parameters
        ----------
        results : dict
            A dictionary with the calculated results
        """

        for result in results:
            print(result)

        return results


    def jsonFormat(self, results: list) -> dict:
        """
        Method for formatting the results into a json convertable format
        """
        
        jsonFormatedResults = {}
        for result in results:
            id_Name, pay_Currency = result.split(": ")
            pay, currency = pay_Currency.split(' ')
            jsonFormatedResults[id_Name] = [pay, currency]
        return jsonFormatedResults


    def fileOutputName(self) -> str:
        """This is a method for testing purposes. It returns the name of the file that is going to be written"""

        return self._path