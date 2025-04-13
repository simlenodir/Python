# Creating Account class
class Accaount:  
# Initializing Class
    def __init__(self, account_number, accoun_name, balance = 0):
        self.account_number = account_number
        self.account_name = accoun_name
        self.balance = balance 
    
    # Deposit money
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {self.account_number} {amount} and balance = {self.balance}")
    

# Creating Bank Class
class Bank:
# Initializing 
    def __init__(self):
        self.accounts = []
# Adding account
    def add_account(self, account_number, account_name, balance = 0):
        for acc in self.accounts:
            if acc.account_number == account_number:
                print(f"This {account_number} already exists")
            else:
                new_account = Accaount(account_name, account_number, balance)
                self.accounts.append(new_account)
                break

# Running menu 
def print_menu():
    print("\nBank Account Management Menu:")
    print("1. Add an account")
    print("2. List all accounts")
    print("3. deposit money")
    print("4. withdraw money")
    print("5. Account details")
    print("6. Exit")

    choice = input("Enter your choice 1-7")

    if choice == '1':
        account_name = input('Enter your name: ')
        account_number = input('Enter Account Number: ')
        account_balance = input('Enter your amount')
        Bank.add_account(int(account_number), account_name, float(account_balance))

# Running main codes
while True:
    a = print_menu()

    break
