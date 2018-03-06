# -*- coding:utf-8 -*-

# @Author zpf
"""
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
"""


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        elif rowIndex > 1:
            a = [1, 1]
            i = 2
            while i < rowIndex + 1:
                temp = [1]
                j = 0
                while j < i - 1:
                    temp.append(a[j] + a[j+1])
                    j += 1
                temp.append(1)
                a = temp
                i += 1

            return a

if __name__ == "__main__":
    sample = Solution()
    print(sample.getRow(rowIndex=2))
