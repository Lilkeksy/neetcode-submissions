class Solution:
	def removeDuplicates(self, nums: List[int]) -> int:
		
		k = 0
		for i in range(len(nums) - 1, 0, -1):
			if nums[i] == nums[i - 1]:
				k+=1
				
				nums.pop(i)
		
		
		return len(nums)