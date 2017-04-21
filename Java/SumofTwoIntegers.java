package LeetCode.Java;

/**
 * Created by Vonzpf on 17/4/21.
 */
/**-------------------------Title---------------------------------
 Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

 Example:
 Given a = 1 and b = 2, return 3.
 */
public class SumofTwoIntegers {
    public int getSum(int a, int b) {
        if(b == 0)
            return a;
        int sum;
        int carry;
        sum = a^b;
        carry = (a&b)<<1;
        return getSum(sum,carry);
    }
}
