class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Problem: Valid Anagram
        # Link: https://leetcode.com/problems/valid-anagram/
        
        return sorted(s) == sorted(t)

# Sample case:
s = "anagram"
t = "nagaram"

# Create an instance of the Solution class
solution = Solution()

result = solution.isAnagram("anagram", "nagaram")
print(result)

#Output
# True