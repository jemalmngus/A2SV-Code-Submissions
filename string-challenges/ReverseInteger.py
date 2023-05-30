
"""
LeetCode Problem: Reverse Integer
Problem Link: https://leetcode.com/problems/reverse-integer/

Sample Cases:
1. Input: 123
   Output: 321

2. Input: -123
   Output: -321
"""

class Solution:
    def reverse(self, x: int) -> int:
        if x>0:
            x=str(x)[::-1]
            if int(x)>2**31-1:
              return 0
                
            return int(x)
        else:
            x=-x
            x=int(str(x)[::-1])
            if x>2**31-1:
              return 0


            return -x
solution = Solution()
print(solution.reverse(210))  #Output 12