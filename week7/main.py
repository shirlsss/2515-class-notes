from bank_account import BankAccount

acc1 = BankAccount()
print(type(acc1))

print(acc1.balance)

acc2=BankAccount(holder="Kyle",number=20,balance=200000)
