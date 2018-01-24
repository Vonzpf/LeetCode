# -*- coding:utf-8 -*-

# @Author zpf
"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a, 2) + int(b, 2)).replace("0b", '')

if __name__ == "__main__":
    sample = Solution()
    print(sample.addBinary('11', '1'))
