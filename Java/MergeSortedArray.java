package LeetCode.Java;

/**
 * Created by Vonzpf on 17/4/19.
 */
/**-------------------------Title---------------------------------
 Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

 Note:
 You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
 The number of elements initialized in nums1 and nums2 are m and n respectively.
 */
public class MergeSortedArray {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int[] temp = new int[m+n];
        int index = 0;
        int i = 0;
        int j = 0;
        while (i<m && j<n){
            temp[index++] = nums1[i]<nums2[j] ? nums1[i++] : nums2[j++];
        }
        if (i==m&&j!=n){
            while (j < n){
                temp[index] = nums2[j];
                index++;
                j++;
            }
        }
        else if (i!=m&&j==n){
            while (i < m){
                temp[index] = nums1[i];
                index++;
                i++;
            }
        }
        for (int k=0;k<temp.length;k++){
            nums1[k] = temp[k];
        }
    }
}
