

def findTargetIndicesAfterSortingArray(nums,t):
    # res=[]pyijp
    # nums.sort()/kphpp
    # for i,c in enumerate(nums):
    #     if c==t:
    #         res.append(i)
    # return res
    res=[]
    for i in range(len(nums)-1):
        sm=i
        for j in range(i+1,len(nums)):
            if nums[j]<nums[sm]:
                sm=j
        nums[i],nums[sm]=nums[sm],nums[i]
        if nums[i]==t:
            res.append(i)
        elif nums[i]>t:
            break
    if nums[i+1]==t:
        res.append(i+1)
    return res
    
    



# Test the implementation
nums = [2, 0, 2, 1, 1, 0]
res=findTargetIndicesAfterSortingArray(nums,2)
print(res)  # Output: [4,5]

nums = [2, 0, 1]
res=findTargetIndicesAfterSortingArray(nums,0)
print(res)  # Output: [0]


