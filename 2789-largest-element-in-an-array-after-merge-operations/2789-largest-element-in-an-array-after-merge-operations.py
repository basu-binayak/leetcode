class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        index = len(nums)-1
        while index-1>=0:
            if nums[index-1]<=nums[index]:
                nums[index] = nums[index-1] + nums[index]
                nums.pop(index-1)
                index-=1
            else:
                index-=1
        return max(nums)
                
            
                
        