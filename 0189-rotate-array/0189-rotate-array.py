class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)

        if n < 100:

            for i in range(k):
                nums[:] = nums[-1:] + nums[:(n-1)]
            return nums

        else:
            k = k%n
            nums[:] = nums[-k:] + nums[:(n-k)]
            return nums