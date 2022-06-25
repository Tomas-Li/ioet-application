#Constants
from ..const.consts import WEEKDAYS

#Local Classes
from ..components.Containers.ContainerPayments import ContainerPayment
from ..components.Containers.ContainerEmployees import ContainerEmployees

def calculation(payments: ContainerPayment, employees: ContainerEmployees) -> list:
    """
    This function uses a ConatinerPayment and a ContainerEmployees to calculate the total amount to pay to every employee

    Parameters
    ----------
    payments : ContainerPayment
        An instance of ContainerPayment (already loaded)

    employees : ContainerEmployees
        An instance of ContainerEmployees (already loaded)
    """
    results = [];
    for index, employ in enumerate(employees.container):
        #employ's structure is [name, {"day": [[schedule1], [schedule2]], "day": ...]}]
        pay = 0
        for day in WEEKDAYS:
            if day in employ[1].keys():
                for schedule in employ[1][day]:
                    start = schedule[0];
                    finish = schedule[1];

                    try:
                        if start < finish:
                            for hour in list(range(start, finish)):
                                pay += payments.container[day][hour]
                        else:
                            for hour in (list(range(start, 24)) + list(range(0, finish))):
                                pay += payments.container[day][hour]
                    except(KeyError):
                        print(f"KeyError on calculation.py")
                        print(f"Error while accesing the data of {employ[0]}. This may have happened due to the employee working in an hour in which the company doesn't have a payment defined")
                        print(f"The invalid hour was at {hour} on {day}")
                        print(f"{employ[0]}'s data will stop being processed. The calculated amount until this point will be provided at the end")
                        print()
            
        results.append(f"{index}-{employ[0]}: {pay} USD")
    
    return results
