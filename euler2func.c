#include <stdio.h>
#include <euler2.h>

int sumFibonacci(int A) {
    int prev = 1;
    int curr = 2;
    int next;
    int sum = 0;

    while( curr < A ){
        if( curr%2 == 0 ){
            sum += curr;
        }

        next = prev + curr;
        prev = curr;
        curr = next;
    }

    return sum;
}