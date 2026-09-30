from collections import Counter

def get_letter_frequency(string):
    counter = Counter(string)
    for key, value in counter.items():
        print(f'{key}: {value}')

if __name__ == '__main__':
    get_letter_frequency(string)