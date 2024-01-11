# Exercise 1: Car Manufacturing Software
# You are an engineer at a car manufacturing company. Your task is to develop software
# that can handle the creation of different types of cars (Sedan, SUV, Hatchback) with
# various customizations (color, engine type, accessories).

#Builder Design Pattern

class Car:
    def __init__(self):
        self.model = None
        self.color = None
        self.engine_type =  None
        self.accessories = []     # accessories are a list

    def __str__(self):
        return f"{self.color} {self.model} {self.engine_type}"

#mY bUILDER design pattern
class CarBuilder:
    def _init__(self):
        self.car = Car()

    def set_model(self):
        pass

    def set_color(self):
        pass

    def set_engine_type(self):
        pass

    def add_accessories(self):
        pass
    def get_car(self):
        return self.car

class CarDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_car(self):
        self.builder.set_model()
        self.builder.set_color()
        self.builder.set_engine_type()
        self.builder.add_accessories()

class SedanBuilder(CarBuilder):
    def set_model(self):
        self.car.model = "Sedan"
        
    def set_color(self):
        self.car.color = "Yellow"

    def set_engine_type(self):
        self.car.engine_type = "95 Petrol"
    def add_accessories(self):
        self.car.accessories.append("Power steering")

class SUVBuilder(CarBuilder):
    def set_model(self):
        self.car.model = "SUV"
        
    def set_color(self):
        self.car.color = "BALCK"

    def set_engine_type(self):
        self.car.engine_type = "94 PETROL"
    def add_accessories(self):
        self.car.accessories.append ("PANARONOMIC ROOF")   
 
sedan_builder = SedanBuilder()
suv_builder = SUVBuilder()

director_sedan = CarDirector(sedan_builder)
director_sedan.construct_car()
sedan = sedan_builder.get_car()

director_suv = CarDirector(suv_builder)
director_suv.construct_car()
suv = suv_builder.get_car()

# Printing the cars
print(f"Sedan: {sedan}")
print(f"SUV: {suv}")