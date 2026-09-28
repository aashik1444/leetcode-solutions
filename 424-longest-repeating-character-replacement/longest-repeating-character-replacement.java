class Solution {
    public int characterReplacement(String s, int k) {
        int res = 0;
        HashMap<Character, Integer> hm = new HashMap<>();
        int l = 0;
        int f = 0;
        for (int r=0; r<s.length(); r++) {
            hm.put(s.charAt(r), hm.getOrDefault(s.charAt(r),0)+1);
            f = Math.max(f, hm.get(s.charAt(r)));
            if ((r-l+1) - f > k) {
                hm.put(s.charAt(l), hm.get(s.charAt(l))-1);
                l++;
            }
            res = Math.max(r-l+1, res);
        }
        return res;
    }
}