class Solution:
    def deleteElement(self, nums,val):
        i = 0
        while 1:
            if i < len(nums):
                if nums[i] == val:
                    del nums[i]
                else:
                    i = i + 1
            else:
                break
        return len(nums),nums

a = Solution()
print(a.deleteElement([0,1,2,2,3,0,4,2],2))