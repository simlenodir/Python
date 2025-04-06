# Task 1
def is_prime(n: int): 
    if n < 2: return 
    else:
        for i in range(2, int(n ** 0.5) + 1):
           if n % i == 0:
             return f'False: {n} is devided {i} '
        return f'True: {n} is pirme'
print(is_prime(23))

# Task 2
def digit_sum (num):
    str_digit = str(num)
    list_digits = list(str_digit)
    result = 0
    for i in list_digits:
        result += int(i)
    return result
digit_sum(24)

# Task 3
def degrees_two(num):
    k = 1
    while 2 ** k <= num:
        print(2** k, end=' ')
        k +=1
degrees_two(10)  
