# -*- coding:utf-8 -*-

# @Author zpf
"""
We are to write the letters of a given string S, from left to right into lines.
Each line has maximum width 100 units, and if writing a letter would cause the width of the line to exceed 100 units,
it is written on the next line. We are given an array widths, an array where widths[0] is the width of 'a', widths[1] is the width of 'b', ..., and widths[25] is the width of 'z'.

Now answer two questions: how many lines have at least one character from S,
and what is the width used by the last such line? Return your answer as an integer list of length 2.

Note:

The length of S will be in the range [1, 1000].
S will only contain lowercase letters.
widths is an array of length 26.
widths[i] will be in the range of [2, 10].
"""


class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        result = [1, 0]
        value = 0
        for word in list(S):
            new_word = widths[ord(word) - 97]
            if value + new_word > 100:
                result[0] += 1
                value = new_word
            else:
                value += new_word
        result[1] = value
        return result


if __name__ == "__main__":
    sample = Solution()
    print(sample.numberOfLines(widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], S = "bbbcccdddaaa"))
