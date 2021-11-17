from util import *

MAX_AMOUNT = int(1e9)


class bankAccount():
    def __init__(self, ID: int, balance: Amount):
        self.ID = ID
        self.balance = balance

    def withDraw(self, amount: Amount):
        self.balance -= amount

    def deposit(self, amount: Amount):
        if self.balance + amount > MAX_AMOUNT:
            diff = self.balance + amount - MAX_AMOUNT
            self.balance = MAX_AMOUNT
            return diff
        else:
            self.balance += amount
            return 0

    def transfer(self, amount: Amount, toAccount: 'bankAccount'):
        self.withDraw(amount)
        diff = toAccount.deposit(amount)
        if diff > 0:
            self.deposit(diff)
        return diff

    def checkBalance(self):
        return self.balance
