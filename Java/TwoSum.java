package LeetCode.Java;

import java.lang.reflect.Array;

/**
 * Created on 17/3/20.
 */
public class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        int[] Indice = new int[2];

        for(int i = 0; i < nums.length; i++){
            for(int j = i + 1; j < nums.length; j++){
                if(nums[j] == target - nums[i]){
                    Indice[0] = i;
                    Indice[1] = j;
                }
            }
        }
        return Indice;
    }
}