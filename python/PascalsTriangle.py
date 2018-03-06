# -*- coding:utf-8 -*-

# @Author zpf
"""
Given numRows, generate the first numRows of Pascal's triangle.
For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2 :
            return [[1], [1, 1]]
        elif numRows > 2:
            a = [[1], [1, 1]]
            i = 2
            while i < numRows:
                temp = [1]
                j = 0
                while j < i - 1:
                    temp.append(a[i-1][j] + a[i-1][j+1])
                    j += 1
                temp.append(1)
                a.append(temp)
                i += 1

            return a


if __name__ == "__main__":
    Sample = Solution()
    print(Sample.generate(numRows=5))
