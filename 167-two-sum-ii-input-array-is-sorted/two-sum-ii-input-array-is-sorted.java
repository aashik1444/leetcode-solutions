class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int l = 0, r = numbers.length-1;
        while (l<r) {
            int s = numbers[r] + numbers[l];
            if (s > target) r--;
            else if (s < target) l++;
            else return new int[] {l+1, r+1};
        }
        return new int[] {};
    }
}