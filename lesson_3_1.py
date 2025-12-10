class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        
    def info(self):
        return f"Транспортная марка: {self.brand}"
    
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
        
    def info(self):
        return f"{super().info()}, модель: {self.model}"

class EngineCar(Car):
    def __init__(self, brand, model, engine):
        super().__init__(brand, model)
        self.engine = engine
    
    def info(self):
        return f"{super().info()}, двигатель: {self.engine}"  
      
pizda = Vehicle('pizda')
print(pizda.info()) 
car = Car('BMW', 'I8')
print(car.info())
eng1 = EngineCar('BMW', 'I8', 'TURBO')
print(eng1.info())