    # Task 1
def is_leap_year(year: int) -> bool:
    if not isinstance (year, int):
        raise ValueError('Year must be integer')
    return (year % 4 == 0 or year % 100 != 0) or (year % 400 == 0)
print(is_leap_year(2024))

# Task 2
def ifConditions(n: int):
    if n % 2 != 0:
        print('Wird')
    elif n % 2 == 0 and  2 <= n <= 5:
        print('Not wird')    
    elif n % 2 == 0 and 6 <= n <= 20:
        print('Wird')
    elif n % 2 == 0 and n >= 20:
        print('Not wird') 
print(ifConditions(24))        

# Task 3
num = input('Enter your number: ')
n = int(num)
if n % 2 == 1:  # Odd number
    print("Weird")
elif 2 <= n <= 5:  # Even and in range [2, 5]
    print("Not Weird")
elif 6 <= n <= 20:  # Even and in range [6, 20]
    print("Weird")
else:  # Even and greater than 20
    print("Not Weird")

# Task 4
num = input('Enter your number: ')
n = int(num)
if n % 2 == 1:  # Odd number
    print("Weird")
elif 2 <= n <= 5:  # Even and in range [2, 5]
    print("Not Weird")
elif 6 <= n <= 20:  # Even and in range [6, 20]
    print("Weird")
else:  # Even and greater than 20
    print("Not Weird")

# Solution 2
def find_even_numbers_no_if_else(a, b):
    """
    Finds even numbers between a and b (inclusive) without using if-else statements.
    """
    return list(range(a + (a % 2), b + 1, 2)) * (a <= b)  # Returns [] if a > b

# Example usage:
print(find_even_numbers_no_if_else(3, 10))  # Output: [4, 6, 8, 10]
