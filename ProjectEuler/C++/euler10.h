/*
Project Euler
Problem 10
*/
#include <vector>

int64_t sumPrimes(int A);

class Prime{
private:
    std::vector<int> primes;
    void nextPrime();
public:
    Prime();
    ~Prime();
    int primeAtIndex(int A);
};


