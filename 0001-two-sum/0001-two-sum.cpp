class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int i=0,j=0,flag=0;
        for(i=0;i<nums.size();i++){
            for(j=i+1;j<nums.size();j++){
                if(nums[i]+nums[j]==target){
                    flag=1;
                    break;
                }
            }

            if(flag==1){
                break;
            }
        }

        vector<int> val = {i,j};
        return val;
    }
};