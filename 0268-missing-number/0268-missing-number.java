class Solution {
    public int missingNumber(int[] nums) {
        int t = (nums.length * (nums.length + 1) )/ 2;
        int s = 0;

        for(int i =0; i<nums.length ; i++){
            s+=nums[i];
        }
        return t-s;
    }
}