package LeetCode.Java;

/**
 * Created by Vonzpf on 17/3/23.
 */
/**-------------------------Title---------------------------------
 The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

 Given two integers x and y, calculate the Hamming distance.

 Note:
 0 ≤ x, y < 231.

 Example:

 Input: x = 1, y = 4

 Output: 2

 Explanation:
 1   (0 0 0 1)
 4   (0 1 0 0)
        ↑   ↑

 The above arrows point to positions where the corresponding bits are different.
 */
public class HammingDistance {
    public int hammingDistance(int x, int y) {
        int distance = 0;
        String x1 = Integer.toBinaryString(x ^ y);
        for (int i = 0; i < x1.length(); i++){
            if (x1.charAt(i) == '1')
                distance++;
        }
        return distance;
    }
}
