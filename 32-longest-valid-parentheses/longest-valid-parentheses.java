class Solution {
    public int longestValidParentheses(String s) {
        Stack<Integer> stack = new Stack();
        stack.push(-1);
        int mlen = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') stack.push(i);
            else {
                stack.pop();
                if (stack.isEmpty()) stack.push(i);
                else {
                    int l = i - stack.peek();
                    mlen = Math.max(mlen, l);
                }
            }
        }
        return mlen;
    }
}