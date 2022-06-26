#Constants
import json
from constants import WEEKDAYS

#built-in imports
import random

def loadNames()->list:
    """
    Function for loading names from a txt file
    """

    with open('./names.txt', mode='r', encoding='utf-8') as f:
        nameList = []
        for line in f:
            nameList.append(line.replace('\n', ''))
    return nameList


def bellLeft(lista: list, weight: int = 1) -> list:
    """
    Function for defining left sided weigths for a sample

    Parameters:
    ----------
    lista: list
        used to obtain the length of the weight to work

    weigth: int = 1
        for changing the velocity of the curve
    """

    length = len(lista)
    starter = 100
    weights = []
    
    value = starter
    for _ in range(0,length):
        weights.append(value)
        value = (value - int(starter/length))/weight
    return weights


def intervalGenerator(nTurnsMax: int) -> dict:
    """
    Function for calculating intervals in random days of the week

    nTurns: int
        Indicates the maximum number of turns 
    """
    interval = {}
    turnsWeights = bellLeft(list(range(1,nTurnsMax+1)), weight=3) # This weights the probability of having more than one turn on the same day
    days = random.sample(WEEKDAYS, random.randint(1, 7)) # The days are random too
    for day in days:
        nTurns = random.choices(list(range(1, nTurnsMax+1)), turnsWeights, k=1)[0]
        iteration = 1
        interval[day] = []
        turnCalculator(interval, day, nTurns, iteration)
    
    return interval
            


def turnCalculator(interval: dict, day: str, nTurns: int, iteration: int, remainingHours: int = 8, finish: bool | int = False):
    """
    Recursive function for calculating turns in a day

    Pameters:
    --------
    interval: dict
        is the container for the interval data of the employee
    
    day: str
        is the day that is being considered for the turn

    nTurns: int
        is the number of turns than an employee can have 

    iteration: int
        is the number of recursions (used to control that the number of turns isn't being surprass)

    remainingHours: int
        Number of hours than an employee can still work in a day. Starts with 8

    finish: bool | int
        Is the last recursion's finish time. If it's the first recursion then is False
    
    """

    if not finish:
        start = random.randint(0, 23) #someone can start working an hour from 0:00 to 23:00
    else:
        start = finish
    finish = random.randint(start+1,start+remainingHours)
    if not (finish < 25): finish = 24
    interval[day].append(f"{start}-{finish}")

    if finish < 24 and  remainingHours > 0 and nTurns > iteration:
        iteration += 1
        remainingHours -= finish - start
        turnCalculator(interval, day, nTurns, iteration, remainingHours, finish)


def writer(nEmployees: int, format: str):
    """
    Function for writing the employees data into a file.

    Parameters:
    ----------
    nEmployees: int
        number of random employees to generate
    
    format: str
        Format of the output. 'json' | 'txt'
    """

    employees = {}
    with open(f'./DataSamples/employeesSample.{format}', mode='w', encoding='utf-8') as f: #!output
        for _ in range(0, nEmployees):
            name = ' '.join(random.sample(nameList, 2))
            employees[name] = intervalGenerator(3) #!number of intervals per day
        
        if format == 'json':
            json.dump(employees, f, ensure_ascii=False, indent=4)
        


if __name__ == '__main__':
    nameList = loadNames()
    writer(5, 'json') #!number of employees to generate
