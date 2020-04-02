def numberSwapper( a : int, b : int ):
    a = a - b
    b = b + a
    a = b - a
    return a, b

if __name__ == '__main__':
    print(numberSwapper(2,4))