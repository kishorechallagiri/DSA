class Solution {
    public int longestMonotonicSubarray(int[] arr) {
        int n = arr.length;
        int dec = 1;
        int inc = 1;
        int maxval = 1;
        for(int i = 1;i < n;i++){
            if (arr[i] > arr[i-1]){
                inc += 1;
                dec = 1;
            }
            else if(arr[i] < arr[i-1]){
                dec += 1;
                inc = 1;
            }
            else{
                inc = 1;
                dec = 1;
            }
            maxval = Math.max(maxval, Math.max(inc, dec));
        }
        return maxval;

        
    }
}