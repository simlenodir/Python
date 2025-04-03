    # Task 1
def addLineList(text: str): 
    result = []
    count = 0
    lastCharIndex = len(text)
    unli = ['a','e','i','o','u']
    for num,char in enumerate(text):
        result.append(char)
        count += 1
        if count % 3 == 0:
            if lastCharIndex != num + 1 or text[lastCharIndex] != '_':
                if char in unli:
                    if num + 1 < len(text):
                            result.append(text[num + 1])
                            result.append('_')
                else:
                    result.append('_')
            # else:
            #     break

    return "".join(result)
        

addLineList('hdslld_')
# Task 2

def squareOfNumber(number: int): 
     for n in range(number):
          print(n ** 2)

squareOfNumber(5)     

# Task 3-1
i = 0
while i < 10:
    i = i + 1
    print(i)

# Task 3-2
n = 5  
i = 1  # Initialize row counter

while i <= n:
    j = 1  # Initialize number counter for each row
    while j <= i:
        print(j, end=" ")  # Print numbers on the same line
        j += 1
    print()  # Move to the next line
    i += 1  # Increment row counter

# Task 3-3 
num = int(input('Enter any number: '))
i = 0
sum = 0
while i <= num:
     sum += i
print(sum)

# Task 4 
num = 3
for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")


# Task 5
numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
    if i % 5 == 0 and 50 < i <= 150:
        print(i)

# Task 6
number = 9876
listNumber = list(str(number))
count = 0
for i in listNumber:
    count += 1
print (count)    

# Task 7
n = 5
i = n
while i > 0: 
    j = i
    while j >= 1:
        print(j, end= ' ')
        j -= 1
    print()    
    i -= 1

# Task 8
list1 = [10, 20, 30, 40, 50]
for i in range (len(list1) - 1, -1, -1):
    print(list1[i], end=' ')

i = len(list1) - 1
while i >= 0:
    print(list1[i])
    i -= 1
    
# Task 9

i = - 10
while i < 0:
    print(i)
    i += 1  

# Task 10
for i in range(5):
    print(i)
else:
    print('Done')   

# Task 11
for i in range(25, 50, 1):
    for j in range(2, i):
        if i % j == 0:
            break
    else :
        print (i)

# Task 12
x = 0
y = 1
for num in range(10):
    print(x, end= ' ')
    x, y = y, x + y
    
# Task 13
def findFactorial(n: int) -> int:
    result = 1
    for i in range (1, n + 1):
     result = result * i
    return result
print(findFactorial(6))  

# Task 4
list1 = [1, 1, 2]
list2 = [2, 3, 4]
result = []

for i in list1:
    if i not in list2:
        print(i)
        result.append(i)

for j in list2:
    if j not in list1:
        result.append(j)
print(result)        
