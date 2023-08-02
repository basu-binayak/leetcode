class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        # the approach to this problem is simple: instead of going from left
        # to right through nums list , move from right to left. The reason
        # for this is the condition that we are checking! 
        # if nums[i]<=nums[i+1] , replace nums[i+1] by nums[i]+nums[i+1] and 
        # delete nums[i]
        index = len(nums)-1
        
        # check if there exists an index-1 position in list 
        while index-1>=0:
            if nums[index-1]<=nums[index]:
                nums[index] = nums[index-1] + nums[index]
                nums.pop(index-1)
                # note
                # consider [2,3,7,9,3]
                # after one iteration in while loop, the nums= [2,3,16,3]
                # index equals 3. We want the index to point at the newly 
                # formed elelemnt i.e. 16. So must decrease the index by 1
                # since one element is deleted. 
                index-=1   
            else:
                index-=1
        return max(nums)
                
            
                
        