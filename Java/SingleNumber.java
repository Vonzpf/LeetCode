package LeetCode.Java;

import java.util.HashMap;

/**
 * Created by tank on 17/3/25.
 */
/**-------------------------Title---------------------------------
 Given an array of integers, every element appears twice except for one. Find that single one.

 Note:
 Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

 Subscribe to see which companies asked this question.
 */
public class SingleNumber {
    public int singleNumber(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++){
            if (!map.containsKey(nums[i]))
                map.put(nums[i], 1);
            else
                map.replace(nums[i], 2);
        }
        for (Integer key: map.keySet()){
            if (map.get(key) == 1)
                return key;
        }
        return 0;
    }
}

