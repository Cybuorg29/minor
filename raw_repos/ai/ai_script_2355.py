def read_file(filename):
    try:
        with open(filename) as f:
            return f.read()
    except FileNotFoundError:
        print(f"File {filename} was not found.")