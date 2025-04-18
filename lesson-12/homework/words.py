import threading
from collections import Counter
import string

def clean_and_split(text):
    # Replace punctuation (except apostrophes) with spaces and lowercase
    cleaned = ''.join(char if char == "'" or char not in string.punctuation else ' ' for char in text)
    return [word.lower() for word in cleaned.split() if word]

def process_chunk(lines, counter_list, index):
    local_counter = Counter()
    for line in lines:
        words = clean_and_split(line)
        local_counter.update(words)
    counter_list[index] = local_counter

def threaded_word_count(file_path, num_threads=4):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    total_lines = len(lines)
    chunk_size = (total_lines + num_threads - 1) // num_threads  # ceiling division

    threads = []
    counters = [None] * num_threads  # placeholder for each thread's result

    for i in range(num_threads):
        start = i * chunk_size
        end = min(start + chunk_size, total_lines)
        thread = threading.Thread(target=process_chunk, args=(lines[start:end], counters, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    final_counter = Counter()
    for counter in counters:
        if counter:
            final_counter.update(counter)

    return final_counter

# Example usage
if __name__ == "__main__":
    file_path = 'text.txt'  # Replace with your file
    result = threaded_word_count(file_path, num_threads=4)

    # Print summary
    for word, count in result.most_common(40):
        print(f"{word}: {count}")
