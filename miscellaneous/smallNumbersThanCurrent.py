from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums, reverse=True)
        counts = {}
        i, j = 0, 1
     
        while j < len(nums):
          
            if sorted_nums[j] != sorted_nums[i]:
                # Store the count of numbers greater than current element
                counts[sorted_nums[i]] = len(nums) - 1 - i
            
            i += 1
            j += 1
        
        # Store the count of the last element as 0
        counts[sorted_nums[i]] = 0
        result = [counts[num] for num in nums]
        
        return result

# Test case
nums = [8, 1, 2, 2, 3]
solution = Solution()
result = solution.smallerNumbersThanCurrent(nums)
print(result)  # Output: [4, 0, 1, 1, 3]