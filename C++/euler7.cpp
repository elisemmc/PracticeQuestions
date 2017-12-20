/*
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
*/

#include <stdio.h>
#include "euler7.h"

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

        for( std::vector<int>::iterator it = primes.begin(); it < primes.end(); it++){
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
    Prime p = Prime();
    printf( "Answer: %i", p.primeAtIndex( 10001 ) );
    printf( "\n" );

    return(0);
}
