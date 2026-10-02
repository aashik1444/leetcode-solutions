class Solution {
    public String reverseWords(String s) {
        StringBuilder sb = new StringBuilder();
        String[] words = s.split(" ");
        for (String w : words) {
            StringBuilder temp = new StringBuilder(w);
            sb.append(temp.reverse().append(" "));
        }
        return sb.toString().trim();
    }
}