class Solution {
    public String mergeAlternately(String word1, String word2) {
        int a = word1.length();
        int b = word2.length();
        String s = "";
        int min = a > b ? b : a ;
        int i =0;
        for(  ; i<min ; i++){
            s+=word1.charAt(i);
            s+=word2.charAt(i);
        }

        if(a==b){
            return s;
        }else if(a>b){
            for( ; i<a ; i++){
            s+=word1.charAt(i);
            }
        }else {
            for( ; i<b ; i++){
            s+=word2.charAt(i);
            }
        }

        return s;
    }
}