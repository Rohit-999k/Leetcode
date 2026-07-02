class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int a[] = new int[nums1.length+nums2.length];
        int i=0;
        int j=0;
        int k=0;
        while(i<nums1.length && j<nums2.length){
                if(nums1[i]<nums2[j]){
                    a[k++]=nums1[i++];

                }else if(nums1[i]>nums2[j]){
                    a[k++]=nums2[j++];
                    
                }else if(nums1[i]==nums2[j]){
                    a[k++]=nums1[i++];
                }     
        }

        while(i<nums1.length){
            a[k++]= nums1[i++];
        }
        
        while(j<nums2.length){
            a[k++]=nums2[j++];
        }

        if(k%2!=0){
            return a[k/2];
        }else{
            return (float)(a[k/2]+a[(k/2) -1])/2.0;
        }

    }
}