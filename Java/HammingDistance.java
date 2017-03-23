package LeetCode.Java;

/**
 * Created by Vonzpf on 17/3/23.
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
