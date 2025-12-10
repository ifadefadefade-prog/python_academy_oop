class Data():
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        
    def display(self):
        return f"{self.day:02d}.{self.month:02d}.{self.year}"
    
    @classmethod
    def from_string(cls, date_string):
        day, month, year = map(int, date_string.split('.'))
        return cls(day, month, year)
        