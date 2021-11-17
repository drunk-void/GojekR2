from util import *
from bankAccount import *


class Manager():
    def __init__(self):
        self.accounts = {}
        self.transactions = []

    def add_account(self):
        ID = random.randint(1, 10000)
        self.accounts[account.ID] = account
