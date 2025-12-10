class Person:
    def __init__(self, name, old):
        self.name = name
        self.old = old
        
    def greet(self):
        return f"Привет! Меня зовут: {self.name}, мне {self.old} лет"
    
person1 = Person("Кристина", 18)
person2 = Person("Настя", 21)

print(person1.greet())
print(person2.greet())


print(person1.__dict__)
print(person2.__dict__)

person1.hair = 'blond'


print(person1.__dict__)
print(person2.__dict__)