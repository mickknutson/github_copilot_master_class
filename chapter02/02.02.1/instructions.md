# Shot Prompting Exercise

The following are instructions for Java exercise 

## Outline
This exercise contains two directories:
- `lab` contains starter files if any are needed. Might be empty. This is the directory you should perform all your work in. The project and files might not run, and might fail compilation until the lab has been completed. _(See instructions below)_

- `solution` contains completed, and runnable files. Do not perform work in this directory.


---
## Exercise Instructions

## 1. Zero Shot Prompting

Chat with Copilot using the following prompt.

```text
Create a new Python class for an Person.
```

[Person.py](./solution/Person.py)

Creating a function in Javascript

```text
Create a calculator function
```
[calculator.js](./solution/calculator.js)

# 2. One Shot Prompting

Chat with Copilot using the following prompt.

Use copilot to create a class from comments
```text
// create a Person class that is final
// use the final keyword to prevent inheritance
// the class should be based on the encapsulation pattern
// the class should have the following fields
// id, name, age

```
[Person.java](./solution/Person.java), 
[Person.js](./solution/Person.js), 


# 3. Multiple Shot Prompting

Chat with Copilot using the following prompt which includes an example of what we are looking for.

```text
Create a new Python class for an Airplane.

Use the following Car based on C++ code as an example for the Python class:

class Car {
  private:
  string make_name;
  string model_name;
  string registration_number;

  public:
  string getMakeName();
  string getModelName();
  string getRegistrationNumber();
  void drive();
}
```
[Airplane.py](./solution/airplane.py)


---

#### [../back](./README.md)




--- 
# Notes
> TBD



---

#### [../back](../README.md)
