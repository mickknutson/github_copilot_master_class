# Description: this is an airplane class

# Create a new Python class for an Airplane.

# Use the following Car based on C++ code as an example for the Python class:

# class Car {
#   private:
#   string make_name;
#   string model_name;
#   string registration_number;

#   public:
#   string getMakeName();
#   string getModelName();
#   string getRegistrationNumber();
#   void drive();
# }

class Airplane:
    def __init__(self, make_name, model_name, registration_number):
        self.make_name = make_name
        self.model_name = model_name
        self.registration_number = registration_number

    def getMakeName(self):
        return self.make_name

    def getModelName(self):
        return self.model_name

    def getRegistrationNumber(self):
        return self.registration_number

    def fly(self):
        print("Flying...")


# class Airplane:
#     def __init__(self, make, model, year, max_speed):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.max_speed = max_speed
#         self.current_speed = 0

#     def accelerate(self):
#         self.current_speed += 10

#     def decelerate(self):
#         self.current_speed -= 10

#     def stop(self):
#         self.current_speed = 0

#     def get_speed(self):
#         return self.current_speed

#     def __str__(self):
#         return f"{self.year} {self.make} {self.model} with max speed {self.max_speed} and current speed {self.current_speed}"