
# create a User datamodel using YAML syntax
# Using tree double quotes to create a multi-line string
"""
- USER
    - id: int primary key
    - name: string not null
    - age: int not null
"""
 
 # create a User class based off the User datamodel
class User:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
 
    def __repr__(self):
        return f'User({self.id}, {self.name}, {self.age})'
    