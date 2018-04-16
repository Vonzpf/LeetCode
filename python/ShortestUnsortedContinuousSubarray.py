# -*- coding:utf-8 -*-

# @Author zpf
"""
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
"""


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = []
        for e in nums:
            temp.append(e)
        temp.sort()
        low = 0
        high = len(nums) - 1
        flag = 0
        while low < len(nums) and high > 0:
            if nums[low] == temp[low]:
                low += 1
            else:
                flag = 1
                if nums[high] == temp[high]:
                    high -= 1
                else:
                    flag = 1
                    break
        if flag:
            return high - low + 1
        else:
            return 0


if __name__ == "__main__":
    sample = Solution()
    print(sample.findUnsortedSubarray([2]))
