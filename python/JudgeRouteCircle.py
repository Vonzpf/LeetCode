# -*- coding:utf-8 -*-

# @Author zpf
"""
Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true
Example 2:
Input: "LL"
Output: false
"""


class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        word = list(map(lambda x: moves.count(x), list('UDLR')))
        return True if word[0] == word[1] and word[2] == word[3] else False


if __name__ == "__main__":
    sample = Solution()
    print(sample.judgeCircle(moves='UD'))
