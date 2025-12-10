class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        
    def deposite(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Внесено {amount} руб. Новый баланс: {self.balance} руб."
        return "Сумма депозита должна быть положительной"   
        
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                return f"Выведено {amount} руб. Новый баланс: {self.balance} руб."
        return "Сумма вывода должна быть положительной и не быть больше баланса"   
        
    def get_balance(self):
        #return f"Баланс счета {self.owner}: {self.balance} руб."
        return self.balance
    
    
account = BankAccount("Иван Петров", 1000)
print(account.get_balance())
print(account.deposite(500))
print(account.withdraw(200))
print(account.withdraw(2000))     