class BankAccount:
    def __init__(self, initial_balance = 0):
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

account = BankAccount(100)
account.deposit(200)
account.withdraw(50)
print(account.get_balance())