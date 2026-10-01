class Solution {
    public int subtractProductAndSum(int n) {
        int a = 0, sum = 0, prod = 1;
        while (n > 0) {
            a = n % 10;
            sum += a;
            prod *= a;
            n = n / 10;
        }
        return prod - sum;
    }
}