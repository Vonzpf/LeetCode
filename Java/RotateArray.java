package LeetCode.Java;

/**
 * Created by tank on 17/4/8.
 */
/**-------------------------Title---------------------------------
 Rotate an array of n elements to the right by k steps.

 For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
 */
public class RotateArray {
    public int[] rotate(int[] nums, int k) {
        k = k % nums.length;
        if(k==0);
        else {
            int[] temp = new int[k];
            int m = 0;
            for (int i = nums.length-k; i < nums.length; i++, m++){
                temp[m] = nums[i];
            }
            for (int l = nums.length-k-1; l >= 0 ; l--){
                nums[l + k] = nums[l];
            }
            for (int j = 0; j < temp.length; j++){
                nums[j] = temp[j];
            }
        }
        return nums;
    }
}
