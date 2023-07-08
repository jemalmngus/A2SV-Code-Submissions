"""Given an array of integers representing objects 
colored red (0), white (1), and blue (2), 
the task is to sort the objects in-place
 such that objects of the same color are adjacent,
without using the library's sort function."""

def sortColors(nums):
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:
        print(nums)
        if nums[mid] == 0:
            nums[mid], nums[low] = nums[low], nums[mid]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

# Test the implementation
nums = [2, 0, 2, 1, 1, 0]
sortColors(nums)
print(nums)  # Output: [0, 0, 1, 1, 2, 2]

nums = [2, 0, 1]
sortColors(nums)
print(nums)  # Output: [0, 1, 2]


