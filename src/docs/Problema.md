**Rules**:
- No External Libraries!
- Built-in libraries are allowed
- Test libraries are allowed

**Objective**: calculate the total amount to pay to an employ according to the day and time they worked

**Payments**:
- Monday - Friday

- 00:01 - 09:00 25 USD

- 09:01 - 18:00 15 USD

- 18:01 - 00:00 20 USD

- Saturday and Sunday

- 00:01 - 09:00 30 USD

- 09:01 - 18:00 20 USD

- 18:01 - 00:00 25 USD


**Abbreviations**:
- *MO*: Monday

- *TU*: Tuesday

- *WE*: Wednesday

- *TH*: Thursday

- *FR*: Friday

- *SA*: Saturday

- *SU*: Sunday

**Input Example** (FROM A .TXT FILE): RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00
- Add a .json format option?
- Add a .csv format option?
- Add an optional one row input from console: name -> ... ; The days of the week will be presented one by one, if that day the person didn't work input anything that isn't a correct time format like (20:00-21:00)

**Output Example**: The amount to pay RENE is: 215 USD
- Print on screen
- Create its own results folder
- Make an output file with a name based on date-time
- Select output format

**Needs**:
- Testing
- Code structure 
- Design pattern

**Once finished**:
- Include a README.md explaining an overview of the solution (architecture, approach, methodology, and instructions about how to run the program locally including the command line to use [Add an example])
- Upload to GitHub and send the link
