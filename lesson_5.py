class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        raise NotImplementedError("Каждое животное должно определить свой звук!") 
    
    def introduce(self):
        return f"Меня зовут {self.name}, и я говорю {self.speak()}"
    
class Dog(Animal):
    def speak(self):
        return 'gaw!'
    
class Cat(Animal):
    def speak(self):
        return 'meow'
    
dog = Dog("Бобик")
cat = Cat("Мурка")
print(dog.introduce())
print(cat.introduce())   