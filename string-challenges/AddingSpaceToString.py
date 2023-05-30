# Problem: String Spacing - Insert Spaces at Given Indices
# Link: https://leetcode.com/problems/adding-spaces-to-a-string/

from typing import List
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ""
        prev = 0

        for sp in spaces:
            res+=(s[prev:sp] + ' ')
            prev = sp

        res+=(s[prev:])
        return res

s = "LeetcodeHelpsMeLearn"
spaces = [8, 13, 15]
output = Solution().addSpaces(s, spaces)
print(output)  # Output: "Leetcode Helps Me Learn"
