from manager import *

bank = Manager()
account = bank.add_account()

print("Welcome to Bank")
option = 0

while option != 4:
    if option == 1:
        amount = input("Enter amount to deposit: ")
        account.deposit(amount)
    elif option == 2:
        amount = input("Enter amount to withdraw: ")
        account.withdraw(amount)
    elif option == 3:
        print("Your balance is: ", account.check_balance())
    elif option == 4:
        print("Thank you for using our bank")
    print("How can we help you?")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Exit")

    option = int(input("Enter your choice: "))
