class BankAccount:
    def __init__(self, holder, number, balance):
        self.number=number
        self.holder=holder
        self.balance=balance
        print("A new bank account has been created")

    def deposit(self, amt):
        self.balance += amt

    def withdraw(self, amt):
        self.balance -= amt

    def __str__(self):
        return f"Bank Account for holder {self.holder}, with account number {self.number}, with balance {self.balance}"
