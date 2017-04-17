package LeetCode.Java;

/**
 * Created by Vonzpf on 17/4/17.
 */
/**-------------------------Title---------------------------------
 Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

 You may assume the integer do not contain any leading zero, except the number 0 itself.

 The digits are stored such that the most significant digit is at the head of the list.
 */
public class PlusOne {
    public int[] plusOne(int[] digits) {
        int count = 0;
        int[] temp = new int[digits.length+1];
        for (int i = digits.length-1; i >= 0; i--){
            if (digits[i]<9){
                digits[i] = digits[i] + 1;
                break;
            }
            else {
                digits[i] = 0;
                count++;
            }
        }
        if (count == digits.length){
            temp[0] = 1;
            for (int j = 1; j < temp.length; j++)
                temp[j] = 0;
            return temp;
        }
        return digits;
    }
}
