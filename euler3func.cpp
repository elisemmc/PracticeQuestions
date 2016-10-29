#include <stdio.h>
#include <vector>
#include <stdint.h>

#include "euler3.h"

int64_t largestPrimeFactor(int64_t A){  
    std::vector<int64_t> primes;
    addPrime(primes);

    while( true ){
        bool cont = true;
        for (std::vector<int64_t>::iterator it = primes.begin() ; it != primes.end(); it++){
            if( A == *it ){
                return A;
            }else if( A % *it == 0 ){
                A = A / *it;
                cont = false;
                break;
            }
        }
        while( cont ){
            addPrime(primes);
            if( A/2 <= primes.back() ){
                return A;
            } else if ( A % primes.back() == 0 ){
                A = A / primes.back();
                cont = false;
            }
        }
    }
}

void addPrime(std::vector<int64_t> & primes){
    bool addnext = false;

    if(primes.size()==0){
        primes.push_back(2);
        primes.push_back(3);
        //printf("2 : 3 : ");
    }

    int64_t i = primes.back()+2;

    while(!addnext){

        addnext = true;

        for( std::vector<int64_t>::iterator it = primes.begin(); it < primes.end(); it++){
            if(i% *it == 0){
                addnext = false;
                break;
            }
        }

        if(addnext == true){
            primes.push_back(i);
            //printf("%lli : ", i);
        }
        else{
            i = i+2;
        }
    }
}

int64_t PrimeFactor(int64_t x, int64_t y = 2)
{
   int64_t result;
   if (y >= x/2) {result = x;}
   else if((x%y)){result = PrimeFactor(x,y+1);}
   else{result = PrimeFactor(x/y);}
   return result;
}

