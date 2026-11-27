class BankAccount():
    def __init__(self,acc_no,acc_type,acc_name,acc_balance):
        self.acc_no = acc_no
        self.type = acc_type
        self.name = acc_name
        self.balance = acc_balance
    def deposit1(amount):
        if amount > 0:
            self.balance += amount
    def withdraw1(amount):
        if 0 < amount < self.balance:
            self.balance -= amount
    def display():
        print("__Account Details__")
        
BankAccount(123456789,"Savings","Nirmal",5000)
BankAccount.display()



number = int(input("\nEnter your Account Number : "))
types = input("Enter your Account Type : ")
name = input("Enter your Account Holder Name : ")
balance = int(input("Enter your Account balance : "))

def money(deposit,balance):
    if deposit > 0:
        balance = balance+deposit
        print(balance)
    else:
        print("Enter a positive value")
deposit = int(input("\nEnter your amount to get deposited : "))

print("\n__Account Details After Deposit__")
print("Account Number : ",number)
print("Account Type : ",types)
print("Account Holder Name : ",name)
print("Account Balance : ",(money(deposit,balance)))

def money1(withdraw,balance):
    if withdraw < balance:
        balance = balance-withdraw
        print(balance)
    else:
        print("Insufficent Balance")
withdraw = int(input("\nEnter your amount to get withdrawn : "))

print("\n__Account Details After Withdraw__")
print("Account Number : ",number)
print("Account Type : ",types)
print("Account Holder Name : ",name)
print("Account Balance : ",(money1(withdraw,balance)))