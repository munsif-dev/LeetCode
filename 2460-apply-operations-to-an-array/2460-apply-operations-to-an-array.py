class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i] * 2
                nums[i+1] = 0

        z = nums.count(0)
        nums[:] = [i for i in nums if i != 0]
        nums[:] = nums + [0]*z

        
        return nums



        