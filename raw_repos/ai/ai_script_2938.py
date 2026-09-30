def reverse_dict(d):
    return {v: k for k, v in d.items()}

if __name__ == '__main__':
    print(reverse_dict({ 1: 'A', 2: 'B', 3: 'C' }))