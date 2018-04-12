# -*- coding:utf-8 -*-

# @Author zpf
"""
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
Note:
1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].
"""


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if k == 1:
            return max(nums)
        else:
            low = 1
            high = low + k - 1
            temp = (sum(nums[:k]) * 1.0) / k
            max_avg = temp
            while low < len(nums) and high < len(nums):
                new_temp = temp + (nums[high] - nums[low - 1]) * 1.0 / k
                max_avg = max(max_avg, new_temp)
                low += 1
                high = low + k - 1
                temp = new_temp
            return max_avg


if __name__ == "__main__":
    sample = Solution()
    print(sample.findMaxAverage(nums=[1,12,-5,-6,50,3], k = 4))
