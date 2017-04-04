package LeetCode.Java;

/**
 * Created by Vonzpf on 17/4/4.
 */

import java.util.HashMap;

/**-------------------------Title---------------------------------
 Given an array of integers, find if the array contains any duplicates.
 Your function should return true if any value appears at least twice in the array,
 and it should return false if every element is distinct.
 */
public class ContainsDuplicate {
    public boolean containsDuplicate(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++){
            if (!map.containsKey(nums[i])){
                map.put(nums[i], 1);
            }
            else{
                return true;
            }
        }
        return false;
    }
}
