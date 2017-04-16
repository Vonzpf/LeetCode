package LeetCode.Java;

/**
 * Created by Vonzpf on 17/4/16.
 */

import java.util.HashMap;

/**-------------------------Title---------------------------------
 Given an array of integers that is already sorted in ascending order,
 find two numbers such that they add up to a specific target number.

 The function twoSum should return indices of the two numbers such that they add up to the target,
 where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

 You may assume that each input would have exactly one solution and you may not use the same element twice.

 Input: numbers={2, 7, 11, 15}, target=9
 Output: index1=1, index2=2
 */
public class TwoSumII {
    public int[] twoSum(int[] numbers, int target) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        int[] Indices = new int[2];
        for (int i = 0; i < numbers.length; i++){
            if(!map.containsKey(numbers[i]))
                map.put(numbers[i], i+1);
        }
        for (int j = 0; j < numbers.length; j++){
            int temp = target - numbers[j];
            if(numbers[j]==temp){
                Indices[0] = j + 1;
                Indices[1] = Indices[0] + 1;
                break;
            }
            else {
                if(map.containsKey(temp)){
                    Indices[0] = j + 1;
                    Indices[1] = map.get(temp);
                    break;
                }
            }
        }
        return Indices;
    }
}
