# Problem: Valid Anagram
# Link: https://leetcode.com/problems/valid-anagram/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

# Sample case:
s = "anagram"
t = "nagaram"

solution = Solution()

result = solution.isAnagram("anagram", "nagaram")
print(result) # Output: True

