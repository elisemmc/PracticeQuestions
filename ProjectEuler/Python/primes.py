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

    def getPrimeFactorization(self, val):
        return self.primeFactorization(val, self.primesList)

    def primeFactorization(self, val, primes):
        primes = [ elem for elem in primes if elem <= val ]
        if val in primes:
            return [ val ]
        else:
            for p in primes:
                if val % p == 0:
                    return [p] + self.primeFactorization(val/p, primes)
        
        while val > self.primesList:
            self.appendNext()
            if val % self.primesList[-1] == 0:
                return [p] + self.primeFactorization(val/p, primes)

    def appendNext(self):
        start = self.primesList[-1] + 2
        while any([ start%elem == 0 for elem in self.primesList ]):
            start = start+1

        with open('primes.csv', 'a') as f:
            f.write(','+str(start))

        self.primesList.append(start)
        return

if __name__ == "__main__":
    p = primes()
    print p.getPrimeFactorization(500)