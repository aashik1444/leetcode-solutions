class Solution {
    public String reverseOnlyLetters(String s) {
        char[] arr = s.toCharArray();
        int l = 0, r = arr.length-1;
        while (l < r) {
            if (!Character.isLetter(arr[l])) l++;
            else if (!Character.isLetter(arr[r])) r--;
            else {
                char temp = arr[r];
                arr[r] = arr[l];
                arr[l] = temp;
                l++;
                r--;
            }
        }
        return new String(arr);
    }
}