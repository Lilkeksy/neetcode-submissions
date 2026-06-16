class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        length = len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                for j in range (i + 1, len(nums)):
                    nums[j-1] = nums [j]

                length -= 1
        return length