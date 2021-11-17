from util import *

MAX_AMOUNT = Amount("1000000000")


class bankAccount():
    def __init__(self, ID: int, balance=" "):
        self.ID = ID
        self.balance = Amount(balance)

    def withdraw(self, amount: str):
        amount = Amount(amount)
        self.balance -= amount
        return "Done"

    def deposit(self, amount: str):
        amount = Amount(amount)
        if self.balance + amount > MAX_AMOUNT:
            diff = self.balance + amount - MAX_AMOUNT
            self.balance = MAX_AMOUNT
            return f"Error: Account full. Deposited {amount-diff} amount to your account and reimbursed the rest."
        else:
            self.balance += amount
            return "Successful"

    def transfer(self, amount: str, toAccount: 'bankAccount'):
        amount = Amount(amount)
        self.withDraw(amount)
        diff = toAccount.deposit(amount)
        if diff > 0:
            self.deposit(diff)
        return diff

    def check_balance(self):
        return self.balance
