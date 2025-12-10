class Animal():
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        return "Звук животного!"
    
    
class Dog(Animal):
    def speak(self):
        return f"{self.name}, говорит: Гав!"
    
animal = Animal("Существо")
dog = Dog("Рекс")

print(animal.speak())

print(dog.speak())  # Вызывает переопределенный метод

print(dog.name)  # Атрибут унаследован от родительского класса
print(animal.name)   