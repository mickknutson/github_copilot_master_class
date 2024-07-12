# Python Program Logging Exercise

This exercise will let you practice using Copilot with Python. 
- You will work with JSON, text, and CSV files to answer basic questions about the data contained within. 
- While doing this, you will be logging the results to a text file.
- These instructions assume you have Python 3 installed. You can use any OS you choose (OS X, Windows,or Linux).


## Part 1 Implement file logging

1. Open the `program.py` and `logger.py` files (or project if you are using PyCharm) in `lab` directory. Notice that the `program.py` file depends upon the `logger.py` file. 
> * [logger.py](./lab/logger.py)
> * [program.py](./lab/program.py)


2. Run `program.py` and observe that it outputs a message warning that logging must be implemented.
```t
python program.py
```

output:

```
******* LOG METHOD SHOULD BE IMPLEMENTED FIRST *******
```

3. Open the `logger.py` file and check out the ***FIVE*** `TODO`s. Add code to implement each of these and remove the warning(s). Note each message should add to the log file, not overwrite it.

> HINT: Look for TODO 1.1 through 1.5



## Part 2 Working with JSON

Turn your attention to the `load_json` method of the `program.py` file. Follow the detailed `TODO`s in the code. You will be loading a file named `python‐course.json`. 

Use the fact that a dictionary is returned from the json module to answer the questions:

- What is the Name of the course?
- How many Engagements are there (an taught session of the course)?
- What is the City and StartDate of each engagement?
- Is the engagement active?

> HINT: Look for TODO 2.1 through 2.3

## Part 3 Working with CSV

Finally, turn your attention to the `load_csv` method of the `program.py` file. Follow the detailed `TODO`s in the code. You will be loading a file named `fx‐seven‐day.csv`. This is the currency exchange rates for a 7 day period. Note that these values are relative to Canadian dollars. Your job will be to answer the question:

- What is the 7 day average for RUPEEs to USD?

Here is rough sketch of the steps needed to answer this:

1. Load `fx‐seven‐day.csv`
> HINT: TODO 3.1, 3.2

1. Parse the CSV into a data structure you can leverage. A dictionary of `key = three‐letter‐code`, `value = dictionary of row values` is a good choice.
> HINT: Review TODO 3.3

2. Find the average of the 7‐day rate for Rupees to Canadian dollars.
> HINT TODO 3.5

3. Find the average of the 7‐day rate for USD to Canadian dollars.
> HINT TODO 3.6

4. Compute Rupees / USD by dividing the two values above.
> HINT TODO 3.7

## Part 4 Unit Testing

Use Copilot to assist you in create a unit test. 


## Part 5 Documentation

Use copilot to add Pydoc comments for each operation used in the app.

---

#### [./back](./README.md)
