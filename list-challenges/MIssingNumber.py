from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # Problem: Missing Number
        # Link: https://leetcode.com/problems/missing-number/

        # The following code is not efficient
        """
        n = max(nums)
        for i in range(0, n):
            if i not in nums:
                return i
        return n + 1
        """

        n = len(nums)
        total_sum = (n * (n + 1)) // 2
        given_sum = sum(nums)
        return total_sum-given_sum


# Sample Cases

solution = Solution()

nums1 = [1, 0, 3]
print(solution.missingNumber(nums1))  # Output: 2

nums2 = [0, 1]
print(solution.missingNumber(nums2))  # Output: 2