class Solution {
    public int[] twoSum(int[] nums, int target) {
       int i = 0,j = nums.length- 1 ;
       while (i<j){
        int val = nums[i] + nums[j];
        if (val == target){
            return new int[]{i + 1, j + 1};

        }
        else if(val > target){
            j--;
        }
        else{
            i++;
        }

       }
       return new int[]{};
        
    }
}