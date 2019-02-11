# Run program in bash with command `python modularExponentiationForLargeNumbers.py < modularExponentiationForLargeNumbers.d`
def main():
    count = input()
    inputArray = []

    for _ in range(int(count)):
        x = [ int(x) for x in input().split(" ")]
        inputArray.append(x)

    [ print( powMod( x[0], x[1], x[2] ) ) for x in inputArray ]

def powMod( A, B, C ):
    retVal = pow( A, B ) % C
    return retVal

if __name__ == "__main__":
    main()