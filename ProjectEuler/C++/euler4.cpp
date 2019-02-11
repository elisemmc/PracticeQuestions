/*
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
*/
#include <cmath>
#include <stdio.h>
#include "euler4.h"

int largestPalindrome(int A){
    int r = 0;
    int lim = ( pow(10,A) );
    //printf( "%i", lim);
    for( int i = 0; i < lim; i++ ){
        for( int j = i; j < lim; j++ ){
            r = isPalindrome( std::to_string( i*j ) ) ? std::max(r,i*j) : r;
        }
    }  
    return r;
}

bool isPalindrome(std::string S){
    if( ( S.length() <= 2 ) && ( S.front() == S.back() ) ){
        return true;
    }
    else if( S.front() != S.back() ){
        return false;
    }
    else{ //S.front() == S.back
        return isPalindrome( S.substr( 1, S.length() - 2 ) );
    }
    return false;
}

int main() {
    printf( "Answer: %i", largestPalindrome( 3 ) );
    printf( "\n" );

    return(0);
}
