# Task 1
fruits = ["Apple", "Banana", "Cherry", "Mango", "Orange"]
print(fruits[2])

# Task 2
fruits1 = ["Olma", "Nok", "Anor"]
fruits.extend(fruits1)

# Task 3
numbers = [1, 2, 3, 4, 5, 6, 7]
firstNumber = numbers[0]
lastNumber = numbers[-1]
middleNumber = numbers[len(numbers) // 2]

# Task 4
# result = (*fruits,)
# result
favorite_movies = ["Inception", "Interstellar", "The Dark Knight", "Avatar", "Titanic"]
result = tuple(favorite_movies)

# Task 5
cities = ["New York", "London", "Paris", "Tokyo", "Berlin"]
if "Paris" in cities:
    print('In list has Paris')
else: print('In list has not Paris')

# Task 6
# result = numbers + numbers
result = [*numbers, *numbers]
print (result)

# Task 7
result = numbers.pop()
result
numbers

# Task 8
numbers =(*numbers,)
numbers

# Task 9
colors = ["red", "blue", "green", "blue", "yellow", "blue", "black"]

count_colours = colors.count('blue')

# Task 10
animals = ("tiger", "elephant", "lion", "zebra", "giraffe")
indexOFLion = animals.index('lion')

# Task 11
animals1 = ("aligator", "snake")
# result = (*animals, *animals1)
# result = animals1 + animals
result = sum((animals1, animals), ())
result

# Task 12
result = len(animals)
result

# Task 13
numList1 = (1, 2, 3, 4, 5)
numList2 = (6, 7, 8, 9, 10)
result = [*numList1]
result

# Task 14
maxNum = max(numList1)
minNum = min(numList2)
print(maxNum, minNum)

# Task 15
listedTuple = [*animals]
listedTuple.reverse()
result = (*listedTuple,)
result
