# Creating and Using Data
Various ways to create data in copilot


## Data
Depending upon your language, there are many ways in Copilot to create data.

- CSV Files
- SQL
- JavaScript
- YAML

## Excercises

1. [Housing Data Exercises](./02.04.2/instructions.md)


### CSV Files
Create a csv file.
```text
// create csv data for 'id, name, phone' with 10 rows of data
// inline autocomplete works for the csv file: type `id` and press tab to autocomplete the header
```
[data.csv](./02.04.1/solution/data.csv)

### SQL
```text
// create csv data for 'id, name, phone' and two contacts
// inline autocomplete works for the csv file: type `id` and press tab to autocomplete the header
```
[data.sql](./02.04.1/solution/data.sql)


### JavaScript
```text
// create csv data for 'id, name, phone' and two contacts
// inline autocomplete works for the csv file: type `id` and press tab to autocomplete the header
```
[data.js](./02.04.1/solution/data.js)



### Python
```text
# create a User datamodel using Yaml syntax
"""
- USER
    - id: int primary key
    - name: string not null
    - age: int not null
"""
```
[data.py](./02.04.1/solution/data.py)

### YAML
```text
person:
  name: John Doe
  age: 30
  address:
    street: 123 Main St
    city: Anytown
    state: Anystate
  hobbies:
    - Reading
    - Coding
    - Hiking
```
[data.yml](./02.04.1/solution/data.yml)



---

#### [./back](./README.md)
