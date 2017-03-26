package LeetCode.Java;

/**
 * Created by Vonzpf on 17/3/25.
 */
/**-------------------------Title---------------------------------
 Write a function that takes a string as input and returns the string reversed.

 Example:
 Given s = "hello", return "olleh".

 Subscribe to see which companies asked this question.
 */
public class ReverseString {
    public String reverseString(String s) {
        int n = s.length();
        char[] ReverseStringChar = new char[n];
        for (int i = n - 1; i >= 0; i--){
            System.out.println(i);
            ReverseStringChar[n-1-i] = s.charAt(i);
        }
        String ReverseString = String.valueOf(ReverseStringChar);
        return ReverseString;
    }
}
