class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.is_running = False
        
    def start_engine(self):
        if not self.is_running:
            self.is_running = True
            return f"{self.make} {self.model}: Двигатель запущен" 
        return f"{self.make} {self.model}: Двигатель уже был запущен"
   
    def stop_engine(self): 
        if self.is_running:
            self.is_running = False 
            return f"{self.make} {self.model}: Двигатель остановлен"
            
        return f"{self.make} {self.model}: Двигатель уже был остановлен"
    
my_car = Car("Toyota", "Corolla")
print(my_car.start_engine())
print(my_car.stop_engine())