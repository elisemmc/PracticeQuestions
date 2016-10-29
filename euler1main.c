/*
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
    The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
*/

#include <stdio.h>
#include <euler1.h>

int main() {

    printf( "Example case: Correct answer is 23\n");
    printf( "Sum of multiples of 3 or 5 less than 10 : %i \n", sumMultiples( 10 ) );
    printf( "\n" );
    printf( "Sum of multiples of 3 or 5 less than 1000 : %i \n", sumMultiples( 1000 ) );

    return(0);
}