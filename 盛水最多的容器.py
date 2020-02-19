def maxWater(nums):
    i, j, res = 0, len(nums) - 1, 0
    while i < j:
        if nums[i] < nums[j]:
            res = max(res, nums[i] * (j - i))
            i+=1
            
        else:
            res = max(res, nums[j] * (j - i))
            j-=1
    return res

a = maxWater([1, 8, 16, 2, 5, 4, 8, 3, 7])
print(a)