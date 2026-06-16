class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool: # this method takes in the num array.
        
        visited = {}

        for i in nums:
            if i in visited:
                return True
            else:
                visited[i] = i
        return False
