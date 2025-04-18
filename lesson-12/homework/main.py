# Starting with bismilah
import threading

# Function Checking number is prime
def is_prime(n):
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0: return False

    for i in range(3, int(n ** 0.5 + 1), 2):
        if n % i == 0:
            return False
    return True

# Sending numbers to is_prime function arguments
def checker_is_prime(start_number, end_number, result):
    for i in range(start_number, end_number+1):
        if is_prime(i):
            result.append(i)
    return result

# Main function Creating Threads and dinite start_number, end_number
def split_threads_range(start_num, end_num, count_threads):
    threads = []
    result = [[] for _ in range(count_threads)]
    total = end_num - start_num + 1
    step = total // count_threads

    for i in range(count_threads):
        start = start_num  + i * step
        end = start_num + (i + 1) * step - 1 if i != count_threads - 1 else end_num
        thread = threading.Thread(target=checker_is_prime, args=( start,  end, result[i]))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    primeres = [num for sublist in result for num in sublist]
    return primeres

if __name__ == '__main__':
    primes = split_threads_range(1, 100, 4)
    print("Prime numbers from 1 to 100:")
    print(primes)


# 1 Creating is prime function
# 2 Start number end number result append prime numbers
# 3 Creating threads Thread count number 

