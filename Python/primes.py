import math

class primes:
    # SHOULD CHECK IF PRIMES.CSV EXISTS
    with open('primes.csv', 'r') as f:
        read_data = f.read()
    primesList = [int(elem) for elem in read_data.split(',')]

    def __init__(self):
        self.index = 0

    def firstPrime(self):
        self.index = 0
        return self.primesList[self.index]
    
    def nextPrime(self):
        self.index = self.index + 1

        while self.index >= (len(self.primesList) - 1):
            self.appendNext()

        return self.primesList[self.index]
    
    def primeAt(self, i):
        while( len(self.primesList) < i ):
            self.appendNext()
        return self.primesList[i-1]

    def primesLessThan(self, val):
        while( self.primesList[-1] < val ):
            self.appendNext()
        return [ elem for elem in self.primesList if elem < val ]
    
    def appendNext(self):
        start = self.primesList[-1] + 2
        while any([ start%elem == 0 for elem in self.primesList ]):
            start = start+1

        with open('primes.csv', 'a') as f:
            f.write(','+str(start))

        self.primesList.append(start)
        return