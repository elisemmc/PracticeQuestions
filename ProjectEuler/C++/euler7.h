/*
Project Euler
Problem 7
*/

#include <vector>

class Prime{
private:
    std::vector<int> primes;
    void nextPrime();
public:
    Prime();
    ~Prime();
    int primeAtIndex(int A);
};
