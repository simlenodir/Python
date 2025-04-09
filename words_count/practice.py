import re
from collections import defaultdict

count_words = defaultdict(int)

try:
    with open('python.txt', 'r') as file:
        text = file.read()

        # clear and split words
        words = re.findall(r'\b[a-zA-Z]+\b', text)
        # print(words)
        
        for word in words:
            count_words[word.lower()] += 1
        
        # Store in dict
        for word, count in count_words.items():
            print(f'{word}: {count}')

except FileNotFoundError:
    print('File is not exist')
