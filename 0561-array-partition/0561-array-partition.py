class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # sort the nums list
        nums.sort()
        
        result=0
        # start iteration and keep step as 2 
        for i in range(0,len(nums),2):
            result+=nums[i]
        
        return result