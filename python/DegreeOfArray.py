# -*- coding:utf-8 -*-

# @Author zpf
"""
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation:
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
"""


class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_dict = {}
        i = 0
        while i < len(nums):
            if nums[i] in num_dict:
                num_dict[nums[i]][0] += 1
                num_dict[nums[i]][2] = i
            else:
                begin = i
                num_dict[nums[i]] = [1, begin, begin]
            i += 1

        min_length = 100000
        max_frequency = -1
        for e in num_dict.values():
            if e[0] == max_frequency:
                min_length = min(e[2] - e[1] + 1, min_length)
            if e[0] > max_frequency:
                max_frequency = e[0]
                min_length = e[2] - e[1] + 1
        return min_length


if __name__ == "__main__":
    sample = Solution()
    print(sample.findShortestSubArray([2, 1]))
