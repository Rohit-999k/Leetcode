#include<limits.h>

bool isPalindrome(int x) {
    
    if(x<0){
        return false;
    }else{
        int temp = x;
        int value = 0;

        while(temp!=0){
            int unit_value = temp%10;
            if(value > (INT_MAX)/10){
                return false;
            }
            value = ((value*10) + unit_value);
            temp = temp/10;
        }

        if(x == value){
            return true;
        }else{
            return false;
        }
    }
}