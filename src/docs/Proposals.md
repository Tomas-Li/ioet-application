#### File that explains the different approaches considered for classes/functions explained in Approach.txt, and the reason why one option has been chosen over the other:

---

## Container Payments (different approaches at how to store the data):
- Every day with 24hs: {MO:{0:25, 1:25, ..., 23:20}, TU:{...}, …}
    - Pros:
        - Everything is worked as a dictionary -> Extremely fast O(1)
        - 7d*24h -> As a maximum I will have 343 entries (7d+168hs+168costs) which is extremely cheap memory wise. With this in mind, it doesn’t make sense to even think about discarding this option in consideration of saving some memory space.
        - Working like this gives an easy access to the data for classes that want to access it
        - Working like this makes the calculation function much easier as the only thing this function will have to do is look for the day and hour worked by an employee, use it to access the specific payment, add it to a counter that is keeping track of how much that employee should be payed.
    - Cons:
        - This approach wouldn’t work in cases with a lot of data, as the costs in hashes and unnecessary data in memory would be huge.

    - Equivalent alternative:
        - Working with lists inside the main dictionary: { 'MO': [25, 25 ..., 20, 20], TU:[..., ...], ...} 
            - Pros:
                - With this approach every hour is an index for accessing the data (container['MO'][5] -> payment for working at 5 on Mondays)
                - Equivalent to the dictionary proposal but without hashes for the hours (still memory wise this could be improved working with intervals)
            - Cons:
                - As said before, memory wise this can be improved working with intervals
                - Personally I see this as a little more “obscure code” while accessing the data instead of the other approach that seems easier for a first time reader


- Every day with list of intervals and payment as [start, finish, cost]. Example: { MO:[[0,9,25], [9,18,15], [18,0,20]], TU:[[...], ...], ... }
    - Pros:
        - As this approach works with intervals, avoids storing unnecessary data (This would be the perfect approach for a big case where saving memory was important)  
            - For this particular case:
                - Best case: 7d with same payment in every hour ->  7days + 21 elements (7 instances of 1 list of 3 elements) = 28 entries
                - Worst case: 7d where every hour has a different payment -> 7 days + 21 elements (7 instances of 24 arrays of 3 elements) = 511 entries
            - I would expect to always fall in situations much more similar to the best case than the worst case.
        - Working with the built-in module “datetime” (specifically its timedelta class) makes working with intervals much easier!

    - Cons:
        - Much more obscure for reading and working with
        - The program would need a system that recognizes which interval the employee is working in (besides that the system should check if the interval is in between two or more different time prices)
        - Working with lists is much slower as it works with O(n) (again as this problem is small this problem doesn’t count)
        - It’s hardly impossible, but as explained numerically before, there may be cases where this approach is even more expensive memory wise than the other ones.  


At the end **I chose the first approach** as it seemed like the easiest one to work with when calculating the total payment and its the most read friendly of all the approaches. May be not the most efficient memory wise, but as explained before, in this particular case doesn’t make sense to discard it as memory optimization is not a problem.


---

## Container employees:
  - A list where every element is an array formed by the name and a dictionary with a structure like \<day>: [interval]. Example: [['Pedro', {'MO':[0,4],'TU':[0,4], ...}], ['Juan', {'MO':[0,4],'TU':[0,4], ...}], ...]
      - There is no risk of overwriting the data of an employee that shares the name with another as the container is working with a list
      - Indexes can be used as ids
      - Working with a list as the base container is a good approach as I have to iterate over the container to calculate the payment for every employee.


  - Using a dictionary with a structure like \<name>: \<schedule> will have the potential problem of overwriting an employee’s data if there is one or more employees with the same name.
      - This can be avoided using an ids system or something equivalent (but this will make the structure more complicated without a real gain)
      - Another problem is the iteration over a dictionary, as I would prefer to output the results in the same orders as they where given, and in a dictionary that is more difficult as they don’t store the order of their elements.

  - Considering other structures doesn’t make sense as:
      - Using sets doesn’t make sense in this case
      - The reading will be done line by line and updating the containers (this discards no mutable data types)


Of course, with all that said, **I chose the first approach**

---

## Reading and data format:
  - The reading will be done from selected files or through the console.
  - These inputs will have the expected “reading format structure” presented below.
  - Employees will accept inputs through json, txt and console(guided format but equivalent to txt)
  - Payment will accept only json data due to the consideration that writing this file should be something occasional and extremely fast.

---

## Reading format structure (proposal):
  - Payments(json): “\<Day>”: [[\<start>, \<finish>, \<cost>], …]
      Example: {"MO": [[0,9,25], [9,28,15], [18,0,20]]}

  - Employees:
      json: “\<Name>”: { “\<Day>”: [“\<start – finish>”, …], ...]
          Example: {“Rene”: { “MO”: [“10:00-12:00”], ... }, ...}

      txt: “\<Name>”=“\<Day>”\<start>-\<finish>, …
          Example: RENE=MO10:00-12:00, TU10:00-12:00, ...



## Calculation (Based on the container approaches selected above):
  - This will be a function that will receive the data containers of payments and employees
  - It will use an accumulator ti keep track of the earnings of each employee
  - It will iterate over each interval and accumulate the earnings per hour
  - It will return an array with the format \<index>-\<name>: \<pay> \<currency> for each employee


## Writer:
  - It will allow us to choose between console, txt and json as the outputs
  - If json or txt are selected, it will write the output in a file with the name \<date>.\<extension>

