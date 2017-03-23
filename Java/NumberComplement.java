package LeetCode.Java;

/**
 * Created by tank on 17/3/23.
 */
public class NumberComplement {
    public int findComplement(int num) {
        String binary = Integer.toBinaryString(num);
        int numberComplement = (int)((long)Math.pow(2, binary.length()) - 1 - num);
        return numberComplement;
    }
}
