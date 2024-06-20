# Description: this is an airplane class

class Airplane:
    def __init__(self, make, model, year, max_speed):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.current_speed = 0

    def accelerate(self):
        self.current_speed += 10
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

    def brake(self):
        self.current_speed -= 10
        if self.current_speed < 0:
            self.current_speed = 0

    def get_speed(self):
        return self.current_speed

    def __str__(self):
        return f"{self.year} {self.make} {self.model} with max speed of {self.max_speed} and current speed of {self.current_speed}"
