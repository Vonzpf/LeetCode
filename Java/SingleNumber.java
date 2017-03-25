package LeetCode.Java;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;

/**
 * Created by tank on 17/3/25.
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

