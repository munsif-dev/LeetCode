class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[:] = [nums[i] for i in range(len(nums)) if i==len(nums)-1 or nums[i]!=nums[i+1]]
        
        print(len(nums))


