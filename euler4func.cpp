#include <string>
#include <algorithm>
#include <cmath>

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

