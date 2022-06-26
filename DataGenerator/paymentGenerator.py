#constants
from constants import WEEKDAYS, BASECONTAINER

#built-in imports
import json
import random


def intervalGenerator() -> list:
    """
    An interval Generator. Returns an array of arrays with an structure of [[start, finish, pay]]
    """

    flag = True
    start = 0
    intervals = []
    
    while flag:
        final = random.randint(start+1,24)
        pay = random.randint(0, 50)
        if final == 24: 
            final = 0
            flag = False
        intervals.append([start, final, pay])
        start = final

    return intervals

def writer() -> None:
    """
    Main code to execute. Writes the generated data into a json file called paymentSample.json
    """
    with open('./DataSamples/paymentSample.json', mode='w', encoding='utf-8') as f: #!output
        payments = BASECONTAINER.copy()
        for day in WEEKDAYS:
            payments[day] = intervalGenerator()
        json.dump(payments, f, ensure_ascii=False)



if __name__ == '__main__':
    writer()