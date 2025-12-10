class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self.__name = name
        else:
            raise TypeError('Имя должно быть str и ненулевым')
    
    
p1 = Person('Vlad', 38)
print(p1.name)
p1.name = 'Vitalik'
print(p1.name)
    
    