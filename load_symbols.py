def get_symbols():
    with open('symbols.txt', 'r') as f:
        symbols = f.read().split()
        return symbols
