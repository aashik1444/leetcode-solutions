class Solution {
    public boolean isPalindrome(int x) {
        int t = x;
        int a = 0;
        int res = 0;
        while (x > 0) {
            a = x % 10;
            res = res * 10 + a;
            x /= 10;
        }
        if (res == t) return true;
        else return false;
    }
}