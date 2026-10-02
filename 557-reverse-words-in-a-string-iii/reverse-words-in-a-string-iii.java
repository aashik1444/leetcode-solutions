class Solution {
    public String reverseWords(String s) {
        String[] words = s.split(" ");
        StringBuilder sb = new StringBuilder();
        for (String w : words) {
            StringBuilder temp = new StringBuilder(w);
            sb.append(temp.reverse().append(" "));
        }
        return sb.toString().trim();
    }
}