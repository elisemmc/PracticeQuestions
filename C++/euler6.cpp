/*
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
*/
#include <stdio.h>
#include <cmath>
#include "euler6.h"

int sumSquareDifference(int A){
    return squareOfSums(A) - sumOfSquares(A);
}

int sumOfSquares(int A){
    int sum = 0;

    for(int i = 1; i <= A; i++){
        sum += pow(i, 2);
    }

    return sum;
}

int squareOfSums(int A){
    int sum = 0;

    for(int i = 1; i <= A; i++){
        sum += i;
    }

    return pow(sum, 2);
}

int main() {
    printf( "Answer: %i", sumSquareDifference( 100 ) );
    printf( "\n" );

    return(0);
}
