package LeetCode.Java;

/**
 * Created by Vonzpf on 17/4/13.
 */
/**-------------------------Title---------------------------------
 Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

 Do not allocate extra space for another array, you must do this in place with constant memory.

 For example,
 Given input array nums = [1,1,2],

 Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
 It doesn't matter what you leave beyond the new length.
 */
public class RemoveDuplicatesFromSortedArray {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0)
            return 0;
        else{
            int indice = 0;
            int value = nums[0];
            for (int i = 1; i < nums.length; i ++){
                if (nums[i] != value){
                    int temp = nums[i];
                    nums[indice + 1] = temp;
                    value = nums[i];
                    indice += 1;
                }
            }
            return indice + 1;
        }
    }
}
