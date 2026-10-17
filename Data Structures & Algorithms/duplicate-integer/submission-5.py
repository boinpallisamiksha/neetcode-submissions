class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for index in range(len(nums)-1):
             if nums[index+1] == nums[index]:
                return True
        return False

            
