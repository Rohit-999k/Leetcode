class Solution {
    public int findPeakElement(int[] nums) {
        int value = nums[0];
        int i=0;
        if(nums.length==1){
            return 0;
        }else if(nums[nums.length-1]>nums[nums.length-2]){
            return nums.length-1;
        }

        while( i<nums.length-1 && nums[i]>=value ){
            value=nums[i];
            i++;
        }
        return i-1;
    }
}