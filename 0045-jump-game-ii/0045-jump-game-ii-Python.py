class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        goal = n-1
        i = 0
        jumps = 0
        while goal != 0:
            if i+nums[i] >= goal:
                goal = i
                i = 0
                jumps += 1
                continue
            i +=1
        return jumps
        