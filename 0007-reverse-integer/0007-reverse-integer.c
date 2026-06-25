#include<limits.h>
int reverse(int x){
    
    if(x<=INT_MIN || x>=INT_MAX){
        return 0;
    }
    int sign =1;

    if(x<0){
        sign=-1;
        x=(-x);
    }
    int val=0;
    
    while(x>0){
        int last = x%10;
        if(val>INT_MAX/10){
            return 0;
        }
        val = val*10 +last;
        x=x/10;
    }
    return val*sign;
}
