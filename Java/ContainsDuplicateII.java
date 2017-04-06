package LeetCode.Java;

/**
 * Created by Vonzpf on 17/4/6.
 */

import java.util.HashMap;

/**-------------------------Title---------------------------------
 Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array

 such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
 */
public class ContainsDuplicateII {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++){
            if (!map.containsKey(nums[i])){
                map.put(nums[i], i);
            }
            else{
                int j = map.get(nums[i]);
                if(i - j <= k ){
                    return true;
                }
                else {
                    map.replace(nums[i], i);
                }
            }
        }
        return false;
    }
}
