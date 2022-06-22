#Built-in modules
import json

#Local modules
from .ContainerInterface import ContainerInterface

class ContainerEmployees(ContainerInterface):
    def __init__(self, containerType: dict | list) -> None:
        """
        Parameters
        ----------
        containerType : dict | list
            An empty container that can work as the core of the instance. It can be a dict or a list
        """

        self._container = containerType
        self._fileType = ''
        

    @property
    def container(self):
        return self._container


    def load(self, path: str) -> None:
        """
        path : str
            A string with the relative path of the file to read (extension .txt included)
        """
        self._fileType = str(path.split('.')[-1])
        if(self._fileType == 'json'):
            self.loadFromJson(path)
        elif(self._fileType == 'txt'):
            self.loadFromTextFile(path)
        elif(self._fileType == ''):
            self.loadFromConsole();
        else:
            raise Exception("In ContainerEmployees: fileType wasn't recognize")


    def loadFromTextFile(self, path: str) -> None:
        """
        Method for loading data from a .txt file, path given through configFile.ini
        The data should follow a format in which every employe has its own row and the squedule should be presented like:
            RAÚL Perez=MO10:00- 12:00, MO14-16, TH20-1, SU20-1

        Parameters
        ----------
        containerType : dict | list
            An empty container that can work as the core of the instance. It can be a dict or a list

        path : str
            A string with the path of the file to read (extension .txt included)
        
        """
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


    def loadFromJson(self, path: str) -> None:
        """
        Method for loading data from a .json file, path given through configFile.ini


        Parameters
        ----------
        containerType : dict | list
            An empty container that can work as the core of the instance. It can be a dict or a list

        path : str
            A string with the path of the file to read (extension .json included)
        
        """
        with open(path, mode='r', encoding='utf-8') as f:
            jsonfile = json.load(f)
            
            for name in jsonfile.keys():
                employeEschedule = {}
                for k,v in jsonfile[name].items():
                    day = k.strip().upper()
                    intervals = []
                    for interval in v:
                        interval = interval.split('-')
                        start = int(interval[0].split(':')[0])
                        finish = int(interval[1].split(':')[0])
                        intervals.append([start,finish])
                    employeEschedule[day] = intervals
                self._container.append([name.strip().upper(), employeEschedule])



    def loadFromConsole(self):
        """
        Method for loading data from console. Selected when no path has been provided through configFile.ini
        """
        print("""
        To introduce cases through the console the pattern will be the following:
            1)Name of the employe (nothing to exit) 
            2)Days will be shown and you should input the work intervals like: MO -> 10:00-12:00, 14:00-16:00
        """)
        while True:
            name = input("Employe's name | Nothing to exit data input: ").strip().upper()
            if not name: break
            #!Weekdays should be imported from const
            weekDays = ['MO', 'TU', 'WE', 'TH', 'FR', 'SA', 'SU']
            schedule = {}
            for day in weekDays:
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