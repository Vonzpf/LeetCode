# -*- coding:utf-8 -*-

# @Author zpf
"""
You're given a matrix represented by a two-dimensional array,
and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.
The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.
If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix;
Otherwise, output the original matrix.

Example 1:                          Example 2:
Input:                              Input:
nums =                              nums =
[[1,2],                             [[1,2],
 [3,4]]                              [3,4]]
r = 1, c = 4                        r = 2, c = 4
Output:                             Output:
[[1,2,3,4]]                         [[1,2],
                                     [3,4]]

Note:
The height and width of the given matrix is in range [1, 100].
The given r and c are all positive.
"""


class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        r1 = len(nums)
        c1 = len(nums[0])
        if r1 * c1 != r * c:
            return nums
        else:
            temp = []
            new_nums = []
            for e in nums:
                for e1 in e:
                    temp.append(e1)
            i = 0
            while i < r:
                new_nums.append(temp[0 + i * c: c + i * c])
                i += 1
            return new_nums


if __name__ == "__main__":
    sample = Solution()
    print(sample.matrixReshape(nums=[[1, 2], [3, 4]], r=1, c=4))
