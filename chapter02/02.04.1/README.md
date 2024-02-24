# X-Shot Prompting for a Python Project

## Zero Shot Prompting

Chat with Copilot using the following prompt.

```text
Create a new Python class for an Person.
```
Use copilot to create a class from comments
```text
// create a person class that is final
// use the final keyword to prevent inheritance
// the class should be based on the encapsulation pattern
// the class should have the following fields
// id, name, age

```
[Person.java](./solution/Person.java), 
[Person.js](./solution/Person.js), 
[Person.py](./solution/Person.py)

Creating a function in Javascript

```text
Create a calculator function
```
Use copilot to create a class from comments
```text
// create a person class that is final
// use the final keyword to prevent inheritance
// the class should be based on the encapsulation pattern
// the class should have the following fields
// id, name, age

```
[calculator.js](./solution/calculator.js)

# One Shot Prompting

Chat with Copilot using the following prompt.

```text
Create a new Python class for an Airplane.
```
Use copilot to create a class from comments
```text
// create a person class that is final
// use the final keyword to prevent inheritance
// the class should be based on the encapsulation pattern
// the class should have the following fields
// id, name, age

```
[Person.java](./solution/Person.java), 
[Person.js](./solution/Person.js), 
[Person.py](./solution/Person.py)


## Multiple Shot Prompting

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

#### [../back](../code.md)
