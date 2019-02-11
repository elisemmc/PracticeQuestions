/*
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
*/
#include <cmath>
#include "euler9.h"

int specialTriplet(){
    int a, b, c;
    for( a = 1; a <= 1000; a++ ){
        for( b = 1; b <= 1000; b++){

            c = sqrt(pow(a,2) + pow(b,2));

            if( pow(a,2) + pow(b,2) == pow(c,2) //make sure we actually have a pythagorean triplet
                && ( a < b ) 
                && ( b < c ) 
                && ( a+b+c == 1000 ) ) //check that we satisfy the specified condition
            {
                return a*b*c;
            }
        }
    }
    return 0;
}

int main() {
    printf( "Answer: %d", specialTriplet() );
    printf( "\n" );

    return(0);
}
