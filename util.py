class Transaction():
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount


class Amount():
    def __init__(self, amount: str = ""):
        self.amount = amount.split()
        self.dollar = int(0)
        self.cent = int(0)
        for i in range(len(self.amount)):
            if amount[i].endswith('D'):
                self.dollar = int(self.amount[i][:-1])
            else:
                self.cent = int(self.amount[i][:-1])

    def __str__(self):
        return str(self.dollar) + 'D ' + str(self.cent) + 'C'

    def __add__(self, other):
        self.dollar += other.dollar
        self.cent += other.cent
        if self.cent > 99:
            self.dollar += self.cent // 100
            self.cent = self.cent % 100
        return self

    def __sub__(self, other: 'Amount'):
        self.dollar -= other.dollar
        self.cent -= other.cent
        if abs(self.cent) > 99:
            temp = abs(self.cent) // 100
            self.dollar -= abs(self.cent) // 100
            self.cent = self.cent + temp*100
        return self

    def __gt__(self, other):
        if self.dollar > other.dollar:
            return True
        elif self.dollar == other.dollar:
            if self.cent > other.cent:
                return True
            else:
                return False
        else:
            return False

    def __lt__(self, other):
        if self.dollar < other.dollar:
            return True
        elif self.dollar == other.dollar:
            if self.cent < other.cent:
                return True
            else:
                return False
        else:
            return False
