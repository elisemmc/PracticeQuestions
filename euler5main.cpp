/*
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
*/

#include <stdio.h>
#include "euler5.h"

int main() {
    printf( "Answer: %i", smallestMultiple( 20 ) );
    printf( "\n" );

    return(0);
}
