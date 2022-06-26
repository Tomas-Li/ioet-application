#### File with ideas to improve the code

- Graphical interface:
	- File selection (more easier than working with the config file, in any case this could be keep as the default file to load)
	- Show results in something better than the console
    - As a built-in option tkinter is more than enough for this implementation.

- More formats:
	- Add csv compatibility

- Add a currency system (needs an API to be accurate):
  - To implement it the step would be:
    - config file should have an input for the payment currency
    - each employ should specify the currency in which they want to get paid
    - from calculation call currencyConversor, a function which using everyemploy's desired currency + input currency converts the result into the correct one
    - use an API to get accurate conversion data from one currency to another
    - use the locale built-in module to work with currencies formats for printing the results

- No static tests (dataGenerator has been writen, but there aren't tests using them):
	- Using dummy data files and predefined variables to check for behaviours works to ensure that everything works, but a more ideal testing case would be done with random values for the data input.
		- Instead of using dummies predefined for reading and checking the data, a more interesting approach would be to define random values for the testings.
		- An example would be using random and a list of names and numbers we could make a variable that represents the employees data, print it in a file, read it and check if the read results are correct. Something similar can be done for testing writing.
		- This can't be used for mathematical testing as the result should be known before hand (so this approach can't be use with calculation() and either with integration tests that uses this function)


- Extra:
    - The built-in module **datetime** was considered as a way to work with containers keeping the data in intervals and not per hour. Using this module is useful in cases where the interval goes over 24h (for example from 22:00 – 2:00) as the classes in this module will know how to work around this.
    - Specifically we should work with **timedelta** instances as they allow us to do algebraic operations between dates, and the same is true for logical operators and this class.