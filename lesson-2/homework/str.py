from datetime import datetime
import re

txt = input("")

# Task 1
name = input("Enter your name: ")
year_of_birth = int(input("Enter your year of birth: "))


current_year = datetime.now().year


age = current_year - year_of_birth

print(f"Hello, {name}! You are {age} years old.")

# Task 2
txt = 'LMaasleitbtui'
result = txt[1::2]
result1 = txt[::2]
print(result, result1)

# Task 3
txt = 'MsaatmiazD'
result = txt[:: -2]
result1 = txt[::2]
print(result1, result)

# Task 4

txt = "I am John. I am from London" 
match = re.search(r'\bfrom (\w+)', txt)

if match: 
    residence = match.group(1)
    print(residence)
else:
    print('No location')

#  Task 5
txt = input("Enter something: ")
reversedTxt = txt[:: -1]
reversedTxt

# Task 6
import re
print (txt)
match = re.findall(r'[aeiouAEIOU]', txt)

if match:
#    Wolwes = match
   countWolwes = len(match)
   print(countWolwes)
else:
   print('No wolwes')

# Task 7
numbers = [1, 2, 3, 4, 5, 11]  
maximum_value = max(numbers)

print(maximum_value) 

# Task 8
txt = 'amma'
reversedTxt1 = txt[:: -1]
if txt == reversedTxt1:
    print(txt + ' is palindrome')
else: print('Its not palindrome')

# Task 9
email = input('Enter your email:')
if '@' in email:
    domain = email.split('@')[1]
    print('Domain: ', domain)
else: print('Invalid email')

# Task 10 
import random
import string

def generate_password(length=12):
    """Generate a random password with letters, digits, and special characters."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Ask user for password length
length = int(input("Enter password length: "))
print("Generated Password:", generate_password(length))
