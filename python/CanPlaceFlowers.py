# -*- coding:utf-8 -*-

# @Author zpf
"""
Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False
Note:
The input array won't violate no-adjacent-flowers rule.
The input array size is in the range of [1, 20000].
n is a non-negative integer which won't exceed the input array size.
"""


class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        num = 0
        temp = 0
        Length = len(flowerbed)
        if Length == 1 and flowerbed[0] == 0:
            if n <= 1:
                return True
        else:
            i = 0
            count = 0
            while i < Length:
                if flowerbed[i] == 0:
                    temp += 1
                else:
                    count += 1
                    if count == 1:
                        num += int(temp/2)
                    else:
                        num += int((temp-1)/2)
                    temp = 0
                i += 1
            if temp != 0:
                num += int(temp/2)
            if temp == Length:
                num = int((temp+1)/2)
            return True if num >= n else False


if __name__ == "__main__":
    sample = Solution()
    print(sample.canPlaceFlowers(flowerbed = [0,0,0], n = 2))
