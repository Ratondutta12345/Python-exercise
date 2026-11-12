# class vehicle:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#     def vehicle_info(self):
#         print("Brand : ",self.brand)
#         print("Model : ",self.model)
# class car(vehicle):
#     pass

# c = car("Toyota","Fortuner")
# c.vehicle_info()


# class vehicle:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#     def vehicle_info(self):
#         print("Brand : ",self.brand)
#         print("Model : ",self.model)
# class car(vehicle):
#     def car_i(self):
#         print("This is a car")

# c = car("Toyota","Fortuner")
# c.vehicle_info()
# c.car_i()


# class vehicle:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#     def vehicle_info(self):
#         print("Brand : ",self.brand)
#         print("Model : ",self.model)
# class car(vehicle):
#     def __init__(self, brand, model,fuel):
#         super().__init__(brand, model)
#         self.fuel = fuel
#     def fuel_type(self):
#         print("Fuel : ",self.fuel)

# c = car("Toyota","Fortuner","petrol")
# c.vehicle_info()
# c.fuel_type()


# class Student:
#     def __init__(self, marks):
#         self.__marks = marks

#     def get_marks(self):
#         print("Marks:", self.__marks)

#     def set_marks(self, new_marks):
#         self.__marks = new_marks

# s1 = Student(70)
# s1.get_marks()

# s1.set_marks(80)
# s1.get_marks()


# class vehicle:
#     def start(self):
#         print("Vehicle is starting")

# class car:
#     def start(self):
#         print("Car is start with a key")

# class bike:
#     def start(self):
#         print("Bike is start using a button")

# vehicles = [car(), bike()]
# for vehicle in vehicles:
#     vehicle.start()