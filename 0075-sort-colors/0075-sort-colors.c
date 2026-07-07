void sortColors(int* nums, int numsSize) {
    for(int i=0;i<numsSize -1 ;i++){
        for(int j=1;j<numsSize;j++){
            if(nums[j-1]>nums[j]){
                int temp = nums[j-1];
                nums[j-1] = nums[j];
                nums[j] = temp;
            }
        }
    }
}