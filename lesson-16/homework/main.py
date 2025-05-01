# Bismillah
import numpy as np
list = [12.23, 13.32, 100, 36.32]
list2 = np.array(list)
print(list2 )

# 2
array = np.arange(2, 11).reshape(3, 3)
print(array)

# 3
vector = np.zeros(10)
vector[6] = 11
print(vector)

# 4
array = np.arange(12, 38)
print(array)

# 5
arr = np.array([1, 2, 3, 4])
print(arr)

float_arr = arr.astype(float)

# 6

# Centigrade values
C = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0.])

# Convert to Fahrenheit
F = C * 9 / 5 + 32

print("Values in Centigrade degrees:", C)
print("Values in Fahrenheit degrees:", F)

# 7
list = [10, 20, 30]

arr = np.array(list)
# print(arr)
arr_1 = [40, 50, 60, 70, 80, 90]

result = np.append(arr, arr_1)
print(result)

 # 8
arr = np.random.rand(10) * 100

# print('Random array:', arr)

mean_val = np.mean(arr)
median_val = np.median(arr)
std_dev = np.std(arr)

print("Mean:", mean_val)
print("Median:", median_val)
print("Standard Deviation:", std_dev)

# 9
# Create a 10x10 array with random values between 0 and 1
arr = np.random.rand(10, 10)

print("10x10 Random Array:\n", arr)

min_val = np.min(arr)
max_val = np.max(arr)

print("Minimum value:", min_val)
print("Maximum value:", max_val)

# 10
# Create a 3x3x3 array with random values between 0 and 1
arr = np.random.rand(3, 3, 3)

print("3x3x3 Random Array:\n", arr)
