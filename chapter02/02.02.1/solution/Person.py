# Description: A Person class

class Person:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
    
    def get_id(self):
        return self.id
    
    def set_id(self, id):
        self.id = id
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
    
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age
