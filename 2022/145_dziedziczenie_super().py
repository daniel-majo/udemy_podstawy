class Result:
    def __init__(self, message, value= None):
        self.isSuccess = None
        self.message = message
        self.value = value

    def is_ok(self):
        return self.isSuccess

class Ok(Result):
    def __init__(self, message, value= None):
        super().__init__(message, value)
        self.isSuccess = True


class Error(Result):
    def __init__(self, message, value= None):
        super().__init__(message, value)
        self.isSuccess = False



class BankAccount:
    def __init__(self, balance=0):
        print('Jestem z klasy rodzic')
        self.balance = balance
    
    def deposit(self, amount):
        """sprawdzamy stan konta"""
        self.balance += amount

    def try_withdraw(self, amount):
        if (self.balance > amount):
            self.balance -= amount
            return Ok("WYpłacono kasę", amount)
        return Error("Niestety brak kasy", amount)
    
    def __str__(self):
        return str(self.balance)
    
class MinimalBalanceAccount(BankAccount):
    def __init__(self, balance=0, minimumBalance=1000):
        # dziedziczenie z klasy
        # BankAccount.__init__(self, balance=0)
        #lub
        super().__init__(balance)
        self.balance = balance
        self.minimumBalance = minimumBalance
    
    def deposit(self, amount):
        """sprawdzamy stan konta"""
        print('Jestem z klasy dziecko')
        self.balance += amount

    
    def try_withdraw(self, amount):
        if (self.balance - amount >= self.minimumBalance):
            return super().try_withdraw(amount)
        else:
            return Error("Nie udało się, przekroczono limit", amount)
    
    def __str__(self):
        return str(self.balance)

konto = BankAccount(500)
print(konto)
konto.try_withdraw(50)
print(konto)
konto.deposit(600)
result = konto.try_withdraw(590)
print(result.message, result.value)

"""KLasa RODZIC (superklasa) - Klasa DZIECKO (subklasa)"""
print('-'*20)
account = MinimalBalanceAccount(1500,1000)
print(account.balance)
account.deposit(1200)
print(account.balance)
result = account.try_withdraw(1701)
# account.try_withdraw(1699)
print(result.message)
print(account.balance)
account.deposit(1500)
print(account.balance)