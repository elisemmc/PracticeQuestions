/*
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
    The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
*/

#include <stdio.h>
#include "euler1.h"

int sumMultiples(int A) {
    int i = 0;
    int sum = 0;

    for( i = 0; i < A; i++ ){
        if( ( i % 3 == 0 ) || ( i % 5 == 0 ) ){
            sum += i;
        }
    }

    return sum;
}

int main() {

    printf( "Example case: Correct answer is 23\n");
    printf( "Sum of multiples of 3 or 5 less than 10 : %i \n", sumMultiples( 10 ) );
    printf( "\n" );
    printf( "Sum of multiples of 3 or 5 less than 1000 : %i \n", sumMultiples( 1000 ) );

    return(0);
}