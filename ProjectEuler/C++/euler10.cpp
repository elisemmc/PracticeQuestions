/*
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
*/
#include "euler10.h"

long long sumPrimes(int A){
    Prime p = Prime();
    long long sum = 0;
    int i = 0;
    while( p.primeAtIndex(i) < A ){
        sum += p.primeAtIndex(i);
        i++;
    }
    return sum;
}

Prime::Prime(){
    primes.push_back(2);
    primes.push_back(3);
}

Prime::~Prime(){}

int Prime::primeAtIndex(int A){
    while(primes.size() < A){
        nextPrime();
    }
    return primes[A-1];
}

void Prime::nextPrime(){
    bool addnext = false;
    int i = primes.back() + 2;

    while(!addnext){

        addnext = true;

        for( std::vector<int>::iterator it = primes.begin(); *it * 2 < i; it++){
            if(i% *it == 0){
                addnext = false;
                break;
            }
        }

        if(addnext == true){
            primes.push_back(i);
        } else {
            i = i+2;
        }
    }
}

int main() {
    printf( "Answer: %lld", sumPrimes(2000000) );
    printf( "\n" );

    return(0);
}
