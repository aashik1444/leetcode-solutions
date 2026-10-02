class Solution {
    public int[] closestPrimes(int left, int right) {

        boolean[] prime = new boolean[right + 1];

        // Initially assume every number >= 2 is prime
        for (int i = 2; i <= right; i++) {
            prime[i] = true;
        }

        // Eliminate composites
        for (int i = 2; i * i <= right; i++) {
            if (prime[i]) {
                for (int j = i * i; j <= right; j += i) {
                    prime[j] = false;
                }
            }
        }

        int prev = -1;
        int first = -1;
        int second = -1;
        int minDiff = Integer.MAX_VALUE;

        for (int i = left; i <= right; i++) {

            if (prime[i]) {

                if (prev != -1) {
                    int diff = i - prev;

                    if (diff < minDiff) {
                        minDiff = diff;
                        first = prev;
                        second = i;
                    }
                }

                prev = i;
            }
        }

        return new int[]{first, second};
    }
}