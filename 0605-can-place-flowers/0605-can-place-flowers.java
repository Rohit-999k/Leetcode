class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int count =0;
        int i= 0 ;
        if (flowerbed.length<=2 && flowerbed[0]==0){
            if(n>1){
                return false;
            }else if(flowerbed.length==1){
                return true;
            }else if(flowerbed[1] == 0){
                return true;
            }
        }

        for( i =2;i<flowerbed.length-2;i++){
            if(flowerbed[i-1]==0 && flowerbed[i]==0 && flowerbed[i+1]==0){
                count++;
                i++;
            }
        }

        if((flowerbed[0]==0 && flowerbed[1]==0)) {
            count++;
        }
        if((flowerbed[flowerbed.length-1]==0) && (flowerbed[flowerbed.length-2]==0)){
            count++;
        }

        return n<=count;
        
    }
}