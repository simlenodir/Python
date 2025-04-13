# Start bank program

# Creating Account class
class Accaount:  
# Initializing Class
    def __init__(self, account_number, account_name, balance = 0):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance 
    
    # Deposit money
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {self.account_number} {amount} and balance = {self.balance}")

    # Withdraw money
    def withdraw (self, amount):
        print(f"{amount}")
        result = self.balance - amount
        print(f'Your balance = {result}')
    
    def __str__(self):
        return f'{self.account_number},{self.account_name},{self.balance}'

# Creating Bank Class
class Bank:
# Initializing 
    def __init__(self, name):
        self.name = name
        self.account_list = []

# Adding account
    def add_account(self, account_number, account_name, balance = 0):
        print(account_number, account_name, balance)
        print('ashjgfdhn')

        if len(self.account_list) == 0:
            new_account = Accaount(account_number,account_name, balance)
            self.account_list.append(new_account)
            print(f'{account_name} your account opened successfuly')
        else:
            for obj in self.account_list:
                if obj.account_number == account_number:
                    print(f"This {account_number} already exists")
                    break
            else:
                    new_account = Accaount(account_number,account_name, balance)
                    self.account_list.append(new_account)
                    print(f'{account_name} your account opened successfuly')
                    
    
# Showing details of account
    def account_detail(self, account_number):
        print(f'{account_number}')
        print(f'{self.account_list}')

        if len(self.account_list) == 0:
            print(f'Account list is empty')
        else:
            for acc in self.account_list:
                if acc.account_number == account_number:
                    print(f'{acc.account_number}, {acc.account_name}, balance: {acc.balance}')
                    break
            else:
                print(f'this {account_number} doesnt exist')

# 3 Check balance
    def check_balance(self, account_number):
        # Checking Account list is empty
        if len(self.account_list) == 0:
            print('Accounts don`t exits would you like create account ?')
            choice = input('Choose yes/no')
            if choice.lower() == 'yes':
                account_name = input('Enter your name: ')
                # account_number = input('Enter Account Number: ')
                account_balance = float(input('Enter your amount: '))
                new_account = Accaount(account_name, account_number, account_balance)
                self.account_list.append(new_account)
            else:
                print("Sorry we will be our customer 😥")
        # IF its not empty
        else:
            for account in self.account_list:
                if account.account_number == account_number:
                    print(f'Your balance: {account.balance}')
                    break
           
            else:
                print('This accounts don`t exits would you like create account ?')
                choice = input('Choose yes/no')
                if choice.lower() == 'yes':
                    account_name = input('Enter your name: ')
                    # account_number = input('Enter Account Number: ')
                    account_balance = float(input('Enter your amount: '))
                    new_account = Accaount(account_name, account_number, account_balance)
                    self.account_list.append(new_account)
                else:
                    print("Sorry we will be our customer 😥")         
# 4 Deposit money

    def deposit(self, account_number, amount):

        for account in self.account_list:
            if account.account_number != account_number:
                pass
            else:
                deposit = amount
                account.deposit(deposit)
                break
        else:
            print('This accounts don`t exits would you like create account ?')
            choice = input('Choose yes/no: ')
            if choice.lower() == 'yes':
                    account_name = input('Enter your name: ')
                    # account_number = input('Enter Account Number: ')
                    account_balance = float(input('Enter your amount: '))
                    new_account = Accaount(account_name, account_number, account_balance)
                    self.account_list.append(new_account)
                    print(f'{new_account}, {self.account_list}')
            else:
                    print("Sorry we will be our customer 😥")    


# 5 Withdraw Money
    def withdraw(self, account_number, amount):
        print(f"{account_number}, {amount}")

        # find account
        for account in self.account_list:
            if account.account_number != account_number:
                pass
            else:
                if account.balance >= amount:
                    account.withdraw(amount)
                    break

# 6 Transfer Money
    def transfer(self, account_number, transfer_number, amount):
        print(f"{account_number}, {transfer_number}, {amount}")
        # Finding Sender and Reciver account
        sender_acc = next((acc for acc in self.account_list if acc.account_number == account_number), None)
        reciver_acc = next((acc for acc in self.account_list if acc.account_number == transfer_number), None)

        if not reciver_acc: 
            print(f'Please Check this {reciver_acc} number doesn`t exist') 
        elif reciver_acc and sender_acc.balance >= reciver_acc.balance:
            sender_acc.balance -= amount
            reciver_acc.balance += amount
            print(f'{sender_acc.balance} - {amount}')
        

bank = Bank('NBU')
# Running menu 
def print_menu():
    print("\nBank Account Management Menu:")
    print("1. Add an account")
    print("2. Display Account Details")
    print("3. Check Balance")
    print("4. Deposit Money")
    print("5. Withdraw Money")
    print("6. Transfer Money")
    print("7. Exit")

    choice = input("Enter your choice 1-7: ")

    if choice == '1':
        account_name = input('Enter your name: ')
        account_number = input('Enter Account Number: ')
        account_balance = float(input('Enter your amount: '))

        bank.add_account(account_number, account_name, account_balance)
    
    # choice 2
    elif choice == '2':
        account_number = input('Enter Account Number: ')
        bank.account_detail(account_number)
    elif choice == '3':
        account_number = input('Enter Account Number: ')
        bank.check_balance(account_number)
    # Choice 4
    elif choice == '4':
#    Choice 5
         account_number = input('Enter Account Number: ')
         amount = float(input("Enter amount: "))
         bank.deposit(account_number, amount)
    elif choice == '5':
        account_number = input('Enter Account Number: ')
        amount = float(input("Enter amount: "))
        bank.withdraw(account_number, amount)

    # Choice 6
    elif choice == '6':
        account_number = input('Enter Your Account Number: ')
        transfer_number = input('Enter Reciver Account Number: ')
        amount = float(input("Enter amount: "))
        bank.transfer(account_number, transfer_number, amount)

# Running main codes
while True:
    a = print_menu()

    break