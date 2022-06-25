## Overview
- This is an application that calculates the payment that an employee should receive given the amount of hours he worked during the week and in which intervals of time he worked.
- The application works with minimum input only requiring from the user to:
    - Set the configuration file (more about this in Configuration and input files-->configFile.ini)
    - Make a payments data file with information about how the company pays in every hour (more aobut this in Configuration and input files-->InputFIles-->Payment data)
    - Make a employees data file with information about how many hours and in which intervals every employee worked during the week (more aobut this in Configuration and input files-->InputFIles-->Payment data)
- The execution only requires to execute the file called clientcode.py on root directory
- The final result will be find in the specified folder in the configuration file and with the corresponding format specified also there


### Notes:
- Look at the **docs folder** for more information about the **approach to the problem**, **explanations about design decisions**, **possible improvments**, and **information about the original problem**
- There as an **abbreviation system** for the weekdays using only the first two character in each day. This is important for the input data format, and will be also used in the output data format.
- **test.py** and **testSamples** have all the code in regardles of tests.

---

## Configuration and input files:
- **configFile.ini**: This is a configuration file at root level in which we should define the following variables
    - PATHPAYMENTS => path to the payments company data (may be a .txt file, a json file, or nothing for console input)
    - PATHEMPLOYEES => path to the employees' working days and hours data
    - PATHOUTPUT => path to output the results (default: './output')
    - OUTPUT_TYPE => output format (may be 'json', 'txt', or 'console')

    Example: 
    ```
        [PATHS]
        PATHPAYMENTS = '../pruebas/dummyPayments.json'
        PATHEMPLOYEES = '../pruebas/dummyLectura.json'
        PATHOUTPUT = './output'

        [OUTPUT]
        OUTPUT_TYPE='jSoN'
    ```

- **Input files**: defined in the configuration file, both of these should have a particular structure for their data:
    - *Payment data*: it has to be a json file in which the keys are the days abbreviations, and the values are a list with nested lists inside, each nested list being a different payment interval during that day. The nested list will have 4 values [\<start hour>, \<finish hour>, \<payment>, \<currency>] (currency may be ignored as is currently not implemented, but this is where it should go as an input).
        - Example: { "MO": [[0,9,25], [9,28,15,"USD"], [18,0,20,"USD"]], ... }
    
    - *Employees data*:
        - **json**: is a dictionary which keys are the employees \<names> (if you have employees with the same name, you may want to use their surnames or something to differentiate them as the json format will only consider the last entry if two or more of them have the same key). The values associated with those keys are other dictonaries wich keys are the days abbreviations and their values are arrays with the intervals in which they have been working each day.
            - Example:     { "Raúl Perez": { "MO": ["10-12", "14-16"], ... }  

        - **txt**: is the format provided in the email: \<name>=\<day abbreviation>\<start>-\<end>, ...
            - Example: RENE = MO 10:00 - 12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00 
        
        - **console**: The inputs will be asked one by one through the console (this can be used with as many employees as the user wants, but the recomendations is to only use it for one employee when having to do a fast run (ideally just write a file and give the path)). The console will ask for the name, then will give a day abreviation in wich a string in the format of \<start>-\<finish>, \<start>-\<finish>, ... should be provided.
        To stop the console input, when asked for a name input an empty string.
            - Example: Name: Raul Perez \n MO -> 10:00-12:00, 14:00-16:00 \n TU -> ...

    - *Notes*:
        - White spaces and uppercases aren't a problem in any of the formats
        - Hours inside the employees data can be input in any of the following formats: [H, HH, HH:MM, HH::MM::SS] (The code always assumes o'clock time as its the logical consideration for the particular problem, so minutes and seconds will be ignored)
        - There are **example files in the examples folder**

---
        
## Instructions:
(Ignore 1 and 2 if you are using the clientcode provided)
1. To run the code use a client code wich imports the Orquestator class from src/components/Orquestator.py
2. Once imported instantiate the class and execute the .run() method as shown in clientcode.py (this is a sample file for showing how to run the code. That's the only function of that file in the root directory)
3. Make sure the configfile and the clientcode are on the same level
4. On a console session at the level of your cliencode run the following command (where \<clientcode.py> is the name of your clientcode file):
    - Windows: python \<clientcode>.py
    - Linux: python \<clientcode>.py

---

## Output:
- The result will be placed inside a folder called output at a root level directory. Each file will have as a name the date-time in wich the code reached and instantiate the Writer class.
- The output format is basically "\<id>-\<name>"=[payment, currency]    (currency is always USD at the moment due to the lack of implementation of a real currency system)

---

## To be careful with:
- JSON files doesn't like non-ASCII characters, so the output file will skip them when writing in this particular format
- JSON files don't like repeated key values, be careful to not have more than one employee with the same name when doing an input with this particular format. If there are cases like this, change to work with the .txt format or add a unique identifier to each employee
- This application has been thought to be used only on windows (or more like with files with explicit extension).