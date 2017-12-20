/*
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
*/

#include <stdio.h>
#include "euler5.h"

int smallestMultiple(int A){
    int r = A;
    while(true){
        bool end = true;
        for( int i = A; i > 0; i-- ){
            if( r%i != 0 ){
                end = false;
                break;
            }
        }
        if( end == true ){
            return r; //program only ends when it finds the smallest multiple
        } else {
            r += A;
        }
    }
}

int main() {
    printf( "Answer: %i", smallestMultiple( 20 ) );
    printf( "\n" );

    return(0);
}
