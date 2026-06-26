#include<limits.h>
double myPow(double x, int n) {
    if(n==0 || x==1 )
    return 1;

    if(x==-1){
        if(n>0){
            return -1;
        }else{
            return 1;
        }
    }

    if(n>=INT_MAX || n<=INT_MIN){
        return 0;
    }
    
    int sign = 1;
    double val=x;
    if(n<0){
        sign = -1;
        n=(-n);
    }
    if(sign!=1){
        x = 1.0/x;
        val = x;
    }

     while(n!=1){
        val = val*x;
        n--;
     }

     return val;



}