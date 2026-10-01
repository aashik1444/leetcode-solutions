class Solution {
    public boolean isHappy(int n) {
        if (n == 1) return true;
        if (n == 4) return false;
        int sum = 0;
        int i = 0;
        while (n > 0) {
            i = n % 10;
            sum += (int)Math.pow(i, 2);
            n /= 10;
        }
        return isHappy(sum);
    }
}