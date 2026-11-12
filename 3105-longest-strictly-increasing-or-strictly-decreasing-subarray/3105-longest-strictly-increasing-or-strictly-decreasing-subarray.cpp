#include<algorithm>
class Solution {
public:
    int longestMonotonicSubarray(vector<int>& nums) {

        int ma=0,mi=0,p = 1,val=nums[0];
        for(int x:nums){
            if(x>val){
                p++;
                
            }else{
                ma = max(p,ma);
                p = 1;
            }
            val = x;
        }
        ma = max(p,ma);
        p=1;
        
        val = nums[0];
        for(int x:nums){
            if(x<val){
                p++;
                
            }else{
                mi = max(p,mi);
                p = 1;
            }
            val = x;
        }
        mi = max(p,mi);

        return max(ma,mi);

        
    }
};