#include<algorithm>
#include<climits>
class Solution {
public:
    int minimumSumSubarray(vector<int>& nums, int l, int r) {
        int s,m=INT_MAX,flag = 0;
        for(int k=l;k<=r;k++){
            for(int i=0;i<=nums.size()-k;i++){
                s = 0;
                for(int j=i;j<k+i;j++){
                    s += nums[j];
                }
                if(s>0){
                    flag  = 1;
                    m = min(s,m);
                }
                

            
            }
        }

        if(flag){
            return m;
        }else {
            return -1;
        }
    }
};