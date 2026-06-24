#include<limits.h>
int divide( int dividend, int divisor) {
    if((dividend>= INT_MAX && divisor==(1))){
        return INT_MAX;
    }else if((dividend<= INT_MIN && divisor==(-1))){
        return INT_MAX;
    }else{
        return(dividend/divisor);
        }
}