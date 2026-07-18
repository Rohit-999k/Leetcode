class Solution {
    public int findGCD(int[] nums) {
        int min =nums[0];
        int max = nums[0];
        for(int i=1;i<nums.length;i++){
            if(nums[i]>max){
                max=nums[i];
            }
            if(nums[i]<min){
                min = nums[i];
            }
        }

        if(max%min==0){
            return min;
        }

        for(int i=min-1;i>0;i--){
            if(max%i==0 && min%i==0){
                return i;
            }
        }

        return 1;
    }
}