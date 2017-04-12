package LeetCode.Java;

/**
 * Created by Vonzpf on 17/4/12.
 */

import java.lang.reflect.Array;
import java.util.Arrays;

/**-------------------------Title---------------------------------
 Given a non-empty array of integers, return the third maximum number in this array.
 If it does not exist, return the maximum number. The time complexity must be in O(n).
 */
public class ThirdMaximumNumber {
    public int thirdMax(int[] nums) {
        int num = 0;
        int thirdMax = 0;
        if (nums.length < 3){
            if (nums.length == 1)
                return nums[0];
            else
                return Math.max(nums[0], nums[1]);
        }
        else {
            Arrays.sort(nums);
            thirdMax = nums[nums.length-1];
            num += 1;
            for (int j = nums.length-2; j >= 0; j--){
                if (nums[j] < thirdMax){
                    thirdMax = nums[j];
                    num += 1;
                }
                if (num == 3)
                    break;
            }
            if (num == 3)
                return thirdMax;
            else
                return nums[0];
        }
    }
}
