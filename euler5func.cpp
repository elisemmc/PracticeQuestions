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

