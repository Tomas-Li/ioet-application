"""
ContainerEmployees.py
--------------------

This file defines the class ContainerEmployees, class in charge of reading and storing all the employees associated data

Attributes:
---------
container
fileType

Methods:
------
load(self, path: str)

loadFromTextFile(self, path: str)

loadFromJson(self, path: str)

loadFromConsole(self)

"""

#Constants
from ...const.consts import WEEKDAYS

#Built-in modules
import json

#Local modules
from .ContainerInterface import ContainerInterface


class ContainerEmployees(ContainerInterface):
    """
    This class defines its main container as a list with the idea of looping through it as every entry should be an employee.
    All the data is loaded through the load method, which calls the correct method implementation for reading based on the file extension of the file to read

    Attributes:
    ----------
    container : list
        Main container of the class. All the employees data is stored here

    Methods:
    --------
    load(self, path):
        This metod calls the correct method to read a file and fill the container attribute
    
    loadFromTextFile(self, path):
        Method for loading data from a .txt file, path given through configFile.ini

    loadFromJson(self, path: str):
        Method for loading data from a .json file, path given through configFile.ini

    loadFromConsole(self):
        Method for loading data from console. Selected when no path has been provided through configFile.ini

    """

    def __init__(self) -> None:
        """
        Starts the class attributes container=[] and filetype=''
        
        """

        self._container = []
        self._fileType = ''
        

    @property
    def container(self):
        return self._container


    def load(self, path: str) -> None:
        self._fileType = str(path.split('.')[-1])
        if(self._fileType == 'json'):
            self.loadFromJson(path)
        elif(self._fileType == 'txt'):
            self.loadFromTextFile(path)
        elif(self._fileType == ''):
            self.loadFromConsole();
        else:
            raise Exception("In ContainerEmployees: fileType wasn't recognize")
            exit()


    def loadFromTextFile(self, path: str) -> None:
        """
        This method should only be accessed from self.load()
        Method for loading data from a .txt file, path given through configFile.ini
        The data should follow a format in which every employee has its own row and the squedule should be presented like:
            RAÚL Perez=MO10:00- 12:00, MO14-16, TH20-1, SU20-1

        Parameters
        ----------
        path : str
             A string for the path with the file to read (extension .txt included)
        
        """

        try:
            with open(path, mode='r', encoding='utf-8') as f:
                for line in f:
                    workingHours = {}
                    name = line.split('=')[0].strip().upper()
                    schedule = line.split('=')[1].replace(' ', '').split(',') #Need to get ride of all posibles spaces in between times
                    for daySchedule in schedule:
                        #schedule's two first characters are the day's identifier follow by the interval separated by a -
                        day = daySchedule[:2].upper()
                        workingInterval = daySchedule[2:].split('-')
                        start = int(workingInterval[0].split(':')[0])
                        finish = int(workingInterval[1].split(':')[0])
                        if day in workingHours.keys():
                            workingHours[day].append([start,finish])
                        else:    
                            workingHours[day] = [[start,finish]]

                    self._container.append([name, workingHours])

        except(FileNotFoundError):
            print("An employees.txt data file couldn't be found at the input path, please check your configFile->PATHEMPLOYEES variable")
            exit()


    def loadFromJson(self, path: str) -> None:
        """
        This method should only be accessed from self.load()
        Method for loading data from a .json file, path given through configFile.ini

        Parameters
        ----------
        path : str
             A string for the path with the file to read (extension .json included)
        
        """

        try:
            with open(path, mode='r', encoding='utf-8') as f:
                jsonfile = json.load(f)
                
                for name in jsonfile.keys():
                    employeeEschedule = {}
                    for k,v in jsonfile[name].items():
                        day = k.strip().upper()
                        intervals = []
                        for interval in v:
                            interval = interval.split('-')
                            start = int(interval[0].split(':')[0])
                            finish = int(interval[1].split(':')[0])
                            intervals.append([start,finish])
                        employeeEschedule[day] = intervals
                    self._container.append([name.strip().upper(), employeeEschedule])
        
        except(FileNotFoundError):
            print("An employees.json data file couldn't be found at the input path, please check your configFile->PATHEMPLOYEES variable")
            exit()


    def loadFromConsole(self) -> None:
        """
        This method should only be accessed from self.load()
        Method for loading data from console. Selected when no path has been provided through configFile.ini
        """

        print("""
        To introduce cases through the console the pattern will be the following:
            1)Name of the employee (nothing to exit) 
            2)Days will be shown and you should input the work intervals like: MO -> 10:00-12:00, 14:00-16:00
        """)
        while True:
            name = input("Employee's name | Nothing to exit data input: ").strip().upper()
            if not name: break
            schedule = {}
            for day in WEEKDAYS:
                intervals = input(f"{day} -> ")
                if not intervals: continue
                intervals = intervals.split(",")
                aux = []
                for interval in intervals:
                    interval = interval.split('-')
                    start = int(interval[0].split(':')[0])
                    finish = int(interval[1].split(':')[0])
                    aux.append([start, finish])
                schedule[day] = aux
            self._container.append([name, schedule])

