class Solution {
    public int smallestIndex(int[] nums) {
        for (int i = 0; i<nums.length; i++) {
            int n = nums[i];
            int ans = 0;
            while (n>0) {
                ans += n%10;
                n = n/10;
            }
            if (ans == i) return i;
        }
        return -1;
    }
}