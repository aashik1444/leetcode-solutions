class Solution {
    public boolean check(int[] nums) {
        int n = nums.length;
        int d = 0;

        for (int i = 0; i < n; i++) {
            if (i < n-1 && nums[i] > nums[i+1]) {
                d++;
            }
            else if ( i == n-1 && nums[n-1] > nums[0]) {
                d++;
            }

            
        }
        return (d > 1) ? false:true;
        
    }
}