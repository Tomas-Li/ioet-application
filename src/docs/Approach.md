#### File explaining the initial approach to the project and the final results:

## Architecture (initial proposal):

0) Orchestrator → commands the execution steps, and is the only part of the code exposed to the client code.

1) Reader -> Interface for the classes in charge of reading the data files (payments and employees)
 - It’s constructor should choose which type of input to read (console or file, if file which format) 
 - This class should be in charge of formatting the data for saving it into containers

2) ContainerInterface -> An interface for the container classes
    1) Class containerPayments -> class in charge of keeping the payment data of the company
    2) Class containerEmployees -> it keeps the information about the name and the worked hours of every employee
    Both of these classes should works as parameters of the next class/function

3) Calculation -> Class/Function that uses both class containers to calculate the total payment

4) Writer -> Class/Function in charge of writing the output

---

## Final Architecture:

0) Orchestrator just as described above.

1) ContainerInterface and its both implementations went as planned, but ended up writing the proposed Reader class as methods for both classes.

2) Calculation ended up as a standalone function as there was no real reason to make it a class over a function.

3) Writer ended up as a class which supports multi format writing.

---

## Testing (initial proposal):
- Orquestador:
    - Test config file lecture and data storing
    - For a final integration testing
    

- Reader:
    - Lecture Dummy to check reading of every possible input

- Containers:
    - Check the data stored into the containers

- Calculation:
    - With dummy data, check the result

- Writer:
    - Capture the output and test it
    - Make the output file and read it to see if it’s correct

- Failure test:
    - Check what happens when an employee work in a time frame not defined by the company (for example the company doesn't open on weekends)
    - Check what happens when an invalid format (output and input) is introduced
