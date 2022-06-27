"""
Testing code for the program. There is a unit-testing section and an integration-testing section separating both kind of tests.
"""
#Built-in imports
import os
import unittest

#Local imports
from src.util.calculation import calculation
from src.components.Containers.ContainerEmployees import ContainerEmployees
from src.components.Containers.ContainerPayments import ContainerPayment
from src.components.Orquestrator import Orquestrator
from src.components.Writer import Writer



#Unit-testings (class cases per module)

class TestContainerEmployees(unittest.TestCase):
    def setUp(self):
        self.containerEmployees = ContainerEmployees()
        self.employee = [
            ['RENE', {'MO': [[10,12]], 'TU': [[10,12]]}],
            ['ASTRID', {'SU': [[20,21]]}],
            ['RAÚL PEREZ', {'MO': [[7,10], [16,20]]}]
        ]

    def test_loadJson(self):
        """
        Testing for load data from a json file for the employees container
        """
        
        self.containerEmployees.load('./testSamples/dummyEmployees.json')

        self.assertEqual(self.containerEmployees.container, self.employee)

    def test_loadTxt(self):
        """
        Testing for load data from a txt file for the employees container
        """

        self.containerEmployees.load('./testSamples/dummyEmployees.txt')
        
        self.assertEqual(self.containerEmployees.container, self.employee)


    ### This test is ommited because it requires manual input through the console
    # def test_loadconsole(self):
    #     self.containerEmployees.load('')

    #     self.assertEqual(self.containerEmployees.container, self.employee)


class TestContainer(unittest.TestCase):
    def setUp(self):
        self.containerPayments = ContainerPayment()
        self.payments = {
            "MO": {0:25, 1:25, 2:25, 3:25, 4:25, 5:25, 6:25, 7:25, 8:25, 9:15, 10:15, 11:15, 12:15, 13:15, 14:15, 15:15, 16:15, 17:15, 18:20, 19:20, 20:20, 21:20, 22:20, 23:20},
            "TU": {0:25, 1:25, 2:25, 3:25, 4:25, 5:25, 6:25, 7:25, 8:25, 9:15, 10:15, 11:15, 12:15, 13:15, 14:15, 15:15, 16:15, 17:15, 18:20, 19:20, 20:20, 21:20, 22:20, 23:20},
            "WE": {0:25, 1:25, 2:25, 3:25, 4:25, 5:25, 6:25, 7:25, 8:25, 9:15, 10:15, 11:15, 12:15, 13:15, 14:15, 15:15, 16:15, 17:15, 18:20, 19:20, 20:20, 21:20, 22:20, 23:20},
            "TH": {0:25, 1:25, 2:25, 3:25, 4:25, 5:25, 6:25, 7:25, 8:25, 9:15, 10:15, 11:15, 12:15, 13:15, 14:15, 15:15, 16:15, 17:15, 18:20, 19:20, 20:20, 21:20, 22:20, 23:20},
            "FR": {0:25, 1:25, 2:25, 3:25, 4:25, 5:25, 6:25, 7:25, 8:25, 9:15, 10:15, 11:15, 12:15, 13:15, 14:15, 15:15, 16:15, 17:15, 18:20, 19:20, 20:20, 21:20, 22:20, 23:20},
            "SA": {0:30, 1:30, 2:30, 3:30, 4:30, 5:30, 6:30, 7:30, 8:30, 9:20, 10:20, 11:20, 12:20, 13:20, 14:20, 15:20, 16:20, 17:20, 18:25, 19:25, 20:25, 21:25, 22:25, 23:25},
            "SU": {0:30, 1:30, 2:30, 3:30, 4:30, 5:30, 6:30, 7:30, 8:30, 9:20, 10:20, 11:20, 12:20, 13:20, 14:20, 15:20, 16:20, 17:20, 18:25, 19:25, 20:25, 21:25, 22:25, 23:25}
        }

    def test_loadJson(self):
        """
        Testing for load data from a json file for the payment container
        """
        self.containerPayments.load('./testSamples/dummyPayments.json')

        self.assertEqual(self.containerPayments.container, self.payments)


class TestWriter(unittest.TestCase):
    def setUp(self) -> None:
        self.result = ['0-RENE: 60 USD', '1-ASTRID: 25 USD', '2-RAÚL PEREZ: 135 USD']

    def test_writerFormat(self):
        """
        Testing for format parsing of data inside writer
        """
        
        writer = Writer('json', './output')
        formatedData = {'0-RENE': ["60", "USD"], '1-ASTRID': ["25", "USD"], '2-RAÚL PEREZ': ["135", "USD"]}

        self.assertEqual(writer.jsonFormat(self.result), formatedData)
    
    def test_writerJson(self):
        """
        Testing for output writing in a json file
        """
        
        writer = Writer('json', './testSamples')
        writer.write(self.result)
        filePath = writer.fileOutputName()
        with open('./testSamples/resultJson.json', mode='r', encoding='utf-8') as f:
            jsonData = f.read()
        with open(f'{filePath}', mode='r', encoding='utf-8') as f:
            jsonWrote = f.read()
        
        self.assertEqual(jsonData, jsonWrote)
        
        #Se elimina el archivo de testing para evitar llenar de basura testSamples
        os.remove(filePath)
    
    def test_writerTxt(self):
        """
        Testing for output writing in a txt file
        """
        
        writer = Writer('txt', './testSamples')
        writer.write(self.result)
        filePath = writer.fileOutputName()
        with open('./testSamples/resultTxt.txt', mode='r', encoding='utf-8') as f:
            txtData = f.read()
        with open(f'{filePath}', mode='r', encoding='utf-8') as f:
            txtWrote = f.read()
        
        self.assertEqual(txtData, txtWrote)

        #Se elimina el archivo de testing para evitar llenar de basura testSamples
        os.remove(filePath)

    ## This method can't fail as it's only a printing over results
    # def test_writerConsole(self):
    #     pass




#Integration-testings:

class TestCalculation(unittest.TestCase):
    def test_calculation(self):
        """
        Calculation testing
        """
        
        self.containerPayments = ContainerPayment()
        self.containerPayments.load('./testSamples/dummyPayments.json')
        self.containerEmployees = ContainerEmployees()
        self.containerEmployees.load('./testSamples/dummyEmployees.json')

        result = ['0-RENE: 60 USD', '1-ASTRID: 25 USD', '2-RAÚL PEREZ: 135 USD']

        self.assertEqual(calculation(self.containerPayments, self.containerEmployees), result)


class TestOrquestrator(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_orquestratorJson(self):
        """
        Entire program execution with json files
        """
        
        filePath = Orquestrator('./testSamples/configFileTestingJson.ini').execute()
        with open('./testSamples/resultJson.json', mode='r', encoding='utf-8') as f:
            jsonData = f.read()
        with open(f'{filePath}', mode='r', encoding='utf-8') as f:
            jsonWrote = f.read()
        self.assertEqual(jsonData, jsonWrote)

        #Se elimina el archivo de testing para evitar llenar de basura testSamples
        os.remove(filePath)
    

    def test_orquestratorTxt(self):
        """
        Entire program execution with txt files
        """
        
        filePath = Orquestrator('./testSamples/configFileTestingTxt.ini').execute()
        with open('./testSamples/resultTxt.txt', mode='r', encoding='utf-8') as f:
            txtData = f.read()
        with open(f'{filePath}', mode='r', encoding='utf-8') as f:
            jsonWrote = f.read()
        self.assertEqual(txtData, jsonWrote)

        #Se elimina el archivo de testing para evitar llenar de basura testSamples
        os.remove(filePath)
    
    
