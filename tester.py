from manager import *

# Test the manager class
bank = Manager()
assert(bank)

# Test the add_account method
account = bank.add_account()
assert(account)

# Test the deposit method success
check = account.deposit("100D 1C")
assert(check == "Successful")

# Test the deposit method failure
check = account.deposit("10000000000D")
assert(check.startswith("Error"))

# Test the withdraw method success
check = account.withdraw("50D 8C")
assert(check == "Done")

# Test the check balance method
check = account.check_balance()
assert(check)
