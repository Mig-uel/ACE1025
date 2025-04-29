"""
Miguel Castillo
Lab 11: Dictionary, Functions, Classes
April 27, 2025
"""


# example 11
# defining a class named 'MyClass'
class MyClass:
    id = 23536481  # property

    def __init__(self):
        pass

    def get_id(self):
        return self.id


# example 12
# constructor in class
class ComplexNumber:
    # constructor
    def __init__(self, real_number, img_number):
        self.r = real_number
        self.i = img_number


# example 13
# create a 'Car' class
class Car:
    # set property 'odometer'
    odometer = 0

    # constructor
    def __init__(self, make, model, year):
        self.car_make = make
        self.car_model = model
        self.car_year = year

    # method to return car info
    def get_car_description(self):
        return f"{self.car_make} {self.car_model} was made in {self.car_year}"

    # method to read the odometer
    def read_odometer(self):
        return f"Odometer reading: {self.odometer}"

    def update_odometer(self, mileage):
        if mileage > self.odometer:
            self.odometer = mileage
        else:
            print("Odometer can not be rolled back")
