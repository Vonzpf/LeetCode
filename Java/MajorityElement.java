package LeetCode.Java;

/**
 * Created by Vonzpf on 17/4/15.
 */

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Objects;

/**-------------------------Title---------------------------------
 Given an array of size n, find the majority element.
 The majority element is the element that appears more than ⌊ n/2 ⌋ times.

 You may assume that the array is non-empty and the majority element always exist in the array.
 */
public class MajorityElement {
    public int majorityElement(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++){
            if (!map.containsKey(nums[i])){
                map.put(nums[i], 1);
            }
            else{
                int temp = map.get(nums[i]);
                temp += 1;
                map.replace(nums[i], temp);
            }
        }
        Iterator iter = map.entrySet().iterator();
        int count = nums.length/2;
        while (iter.hasNext()){
            Map.Entry entry = (Map.Entry) iter.next();
            Object key = entry.getKey();
            Object value = entry.getValue();
            if ( Integer.parseInt(value.toString()) > count)
                return Integer.parseInt(key.toString());
        }
        return 0;
    }
}
