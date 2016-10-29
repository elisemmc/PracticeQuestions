#include <stdio.h>
#include <euler1.h>

/*
    Takes in an integer and returns the sum of 
    all multiples of 3 and 5 less than that integer
*/
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