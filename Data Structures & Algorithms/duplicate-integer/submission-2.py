class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool: # this method takes in the num array.
        
        if len(nums) != len(set(nums)):
            return True
        return False