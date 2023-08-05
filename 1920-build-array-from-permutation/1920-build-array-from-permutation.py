class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        # The main idea is to encode two values at each index of nums, such that we
        # can retrieve the original value and the updated value simultaneously.
        
        n = len(nums)
        # Step 1: encode the items using the formula:
        # encoded_value = nums[i] + n* (nums[nums[i]]%n)
        for i in range(n):
            nums[i] = nums[i] + n *(nums[nums[i]]%n)
            
        # the original value is encoded_value % n
        # the updated value is encoded_value//n
        # note: this updation is possible since here all elements of the nums arr will always be less than n 
        
        # [0,2,1,5,3,4]
        # encoded: 0+6*0=0; 2+6*1=8; 1+6*(8%6)=1+6*2; 5+5*4, 3+6*5; 4+6*3
        
        for i in range(n):
            nums[i] = nums[i]//n
        
        return nums