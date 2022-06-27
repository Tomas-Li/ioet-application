## Overview
- This is an application that calculates the payment that an employee should receive given the amount of hours he worked during the week and in which intervals of time he worked.
- The application works with minimum input only requiring from the user to:
    - Set the configuration file (more about this in Configuration and input files-->configFile.ini).
    - Make a payments data file with information about how the company pays in every hour (more about this in Configuration and input files-->InputFIles-->Payment data).
    - Make a employees data file with information about how many hours and in which intervals every employee worked during the week (more about this in Configuration and input files-->InputFIles-->Payment data).
- The execution only requires to execute the file called clientcode.py at root directory level.
- The final result will be find in the specified folder in the configuration file and with the corresponding format specified also there.


### Notes:
- Look at the **docs folder** for more information about the **approach to the problem**, **explanations about design decisions**, **possible improvements**, and **information about the original problem**
- There is an **abbreviation system** for the weekdays using only the first two character of each day. This is important for the input data format, and will also be used in the output data format.
- **test.py** and **testSamples** have all the code regarding the tests.

---

## Configuration and input files:
- **configFile.ini**: This is a configuration file at root level in which we should define the following variables:
    - PATHPAYMENTS => path to the company payments data (may be 'txt' for a .txt file, 'json' for a json file, or an empty string for console input)
    - PATHEMPLOYEES => path to the employees' working days and hours data
    - PATHOUTPUT => path in which we want the output of the results (default: './output')
    - OUTPUT_TYPE => output format (may be 'json', 'txt', or 'console')

    Example of configFile.ini: 
    ```
        [PATHS]
        PATHPAYMENTS = '../pruebas/dummyPayments.json'
        PATHEMPLOYEES = '../pruebas/dummyLectura.json'
        PATHOUTPUT = './output'

        [OUTPUT]
        OUTPUT_TYPE='jSoN'
    ```

- **Input files**: defined in the configuration file. Both of these files should have a particular structure for their data:
    - *Payment data*: it has to be a json file in which the keys are the days abbreviations and the values are a list with nested lists inside. Each nested list is a different payment interval during that day. The nested list will have 4 values [\<start hour>, \<finish hour>, \<payment>]
        - Example: { "MO": [[0,9,25], [9,28,15], [18,0,20]], ... }
    
    - *Employees data*:
        - **json**: is a dictionary whose the keys are the employees' \<names> (if you have employees with the same name, you may want to use their surnames or something to differentiate them as a json format file will only consider the last entry if two or more of them have the same key). The values associated with those keys are other dictionaries whose keys are the days abbreviations and their values are arrays with the intervals in which they have been working each day.
            - Example:     { "Raúl Perez": { "MO": ["10-12", "14-16"], ... }  

        - **txt**: uses the following format: \<name>=\<day abbreviation>\<start>-\<end>, ...  (this was the format provided in the email)
            - Example: RENE = MO 10:00 - 12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00 
        
        - **console**: The inputs will be asked one by one through the console. First the console will ask for the name, then will give a day abbreviation in which a string in the format of \<start>-\<finish>, \<start>-\<finish>, ... should be provided. This input method can be used with as many employees as the user wants, but the recommendations is to only use it for one employee when having to do a fast run. When there is more than one employee, ideally just write a file and write the path in the configuration file. 
        To stop the console input, when asked for a name input an empty string.
            - Example: Name: Raul Perez \n MO -> 10:00-12:00, 14:00-16:00 \n TU -> ...

    - *Notes*:
        - White spaces and uppercase aren't a problem in any of the input formats
        - Hours inside the employees data can be input in any of the following formats: [H, HH, HH:MM, HH::MM::SS] (The code always assumes o'clock time as its the logical consideration for the particular problem, so minutes and seconds will be ignored)
        - There are **example files in the examples folder**

---
        
## Instructions:
(Ignore steps 1 and 2 if you are using the client code provided)
1. To run the code use a client code file which imports the Orquestator class from src/components/Orquestator.py
2. Once imported, instantiate the class and execute the .run() method as shown in clientcode.py (this is a sample file for showing how to run the code. That's the only function of that file in the root directory)
3. Make sure the configfile and the clientcode are on the same level
4. On a console session at the level of your clientcode run the following command (where \<clientcode.py> is the name of your clientcode file):
    - Windows: python \<clientcode>.py
    - Linux: python \<clientcode>.py

---

## Output:
- The result will be placed inside a folder called output at root level directory. Each file will be named as the date-time in which the code reached and instantiated the Writer class.
- The output format is: "\<id>-\<name>"=[payment, currency]    (currency is always USD at the moment due to the lack of implementation of a real conversion system)

---

## To be careful with:
- JSON files doesn't like non-ASCII characters, so the output file will skip them when writing in this particular format just to avoid strange representations
- JSON files don't like repeated key values, be careful to not have more than one employee with the same name when doing an input with this particular format. If there are cases like this, change to work with the .txt format or add a unique identifier to each repeated employee.
- This application has been thought to be used only on windows (or more like with files with explicit extension).

---

## Testing:
- For executing the tests, run in root level directory: *python -m unittest test.py*
- All tests are in the same file, and they are divided into 2 sections: Unit-tests & Integration-tests

---

## Extra: DataGenerator
- The DataGenerator folder, folder which contains its own code, has been created as a way of having more samples for random testing. Inside there are two python files that will create random data samples to run with the main code.
- To run these files just execute them like normal python files. The output will go into ./DataGenerator/DataSamples
- As these files are just generators, they don't have configuration files neither special design patterns. Important variables that we may want to modify are marked with comments starting with #!