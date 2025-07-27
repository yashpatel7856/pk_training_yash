class Car:
    total_car=0
    def __init__(self,brand,model):
        self.__brand=brand
        self.__model=model
        Car.total_car+=1

    def full_name(self):
        return f"{self.__brand} and {self.__model}"
    
    def get_brand(self): # Encapulation(making the attributes private)
        return self.__brand
    
    
    def fuel_type(self): ## polymorpism
        return "Diesel or Petrol"
    
    @staticmethod
    def general_desc():
        return "something about car"
    
    @property           #after using this decorator now value of model can not be changed and it will be read only 
    def model(self):    
        return self.__model

class Electric_Car(Car): #inheritance
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model) #inheritance
        self.battery_size=battery_size
    def fuel_type(self): #polymorpism
        return "Electric"

safari=Car("tata","safari")
tesla=Electric_Car("Tesla","Model_s",68)

# safari.model="city" # we can now read only the model(property) can not change the value of it after it has been initialize once 
 
# print("asasasasas "+safari.model)
# print(tesla.general_desc())
# print(tesla.fuel_type())
# print(tesla.full_name())
# print(tesla.total_car)


# print(isinstance(tesla,Car))

# class engine:
#     pass
# class battery:
#     pass
# class electricCarTwo(engine,battery):
#     pass

