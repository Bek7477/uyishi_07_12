class Account:
    def __init__(self, id: str, name: str, balance: int = 0) -> None:

        self.id = id
        self.name = name
        self.balance = balance

    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name
    
    def get_balance(self):
        return self.balance
    
    def credit(self, amount):
        self.balance += amount
        return self.balance
    
    def debit(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Amount exceeded balance: ")
        return self.balance
    
    def transfer_to(self, another, amount):
        if amount <= self.balance:
            self.balance -= amount
            another.credit(amount)
        else:
            print("Amount exceeded balance: ")

    def __str__(self):
        return f"Account[id= {self.id}, name= {self.name}, balance= {self.balance}]"
    
account1 = Account("001", "Dilshodbek", 1000)
account2 = Account("002", "Xolmirzayev", 500)

print(account1)
print(account2)

account1.credit(500)
print(account1.get_balance())

account1.debit(200)
print(account1.get_balance())

account1.transfer_to(account2, 300)
print(account1.get_balance())

print(account2.get_balance())
