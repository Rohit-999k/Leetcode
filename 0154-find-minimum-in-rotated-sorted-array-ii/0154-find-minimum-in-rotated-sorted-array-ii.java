class Solution {
    public int findMin(int[] nums) {
        int left=0;
        int right=nums.length-1;
        int mid;
        if(nums.length==1)
            return nums[0];

        while(left<right){
            mid=(left+right)/2;
            if(nums[mid]==nums[right])
                right-=1;
            else if(nums[mid]>nums[right])
                left=mid+1;
            else
                right=mid;
        }
        return nums[left];
    }
}