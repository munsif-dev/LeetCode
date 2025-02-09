class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # size n 
        nums.sort()
        n = len(nums)
        nby2 = int(n/2)
        return nums[nby2]

        

        