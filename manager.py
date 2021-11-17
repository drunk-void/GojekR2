from util import *
from bankAccount import *
from random import randint


class Manager():
    def __init__(self):
        self.accounts = {}
        self.transactions = []

    def add_account(self):
        ID = randint(1, 10000)
        self.accounts[ID] = bankAccount(ID)
        return self.accounts[ID]
