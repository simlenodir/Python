#  Task 1
dic = {"a": 1, "b": 4, "c": 3, "d": 2}
result = sorted(dic.items(), key=lambda x: x[1], reverse=True)
result1 = sorted(dic.items(), key= lambda x: x[1])
print(result1, result)

# Task 2
dicNum = {0: 10, 1: 20}
dicNum[2] = 30
dicNum

# Task 3
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
result = {**dic1, **dic2, **dic3}
# result = dic1 | dic2 | dic3
# result = dic1.update(dic2)
# dic1.update(dic3)
# dic1
result

# Task 4
newDictNum = {x: x **2 for x in range(1, 6)}
newDictNum

# Task 5
newDictNum = {x: x **2 for x in range(1, 6)}
newDictNum

# SET EXIRCISES
# Task 1
my_set = {1, 2, 3, 4, 5, "sgasd", (1, 2, 4,)}
# numbers = set([1, 2, 3, 4, 5])
# print(numbers)

print(my_set)

# Task 2
fruits = {"apple", "banana", "cherry", "mango"}

# Iterating over the set
for fruit in fruits:
    print(fruit)

# Task 3
fruits.add('a')
fruits

# Task 4
newFruits = fruits.remove('a')
print(fruits, newFruits)

# Task 5
# newFruits = fruits.discard('o')
if 'p' in fruits:
    fruits.remove ('p')
else: print("This element is not exists")
print(fruits)
