class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = [1] * len(nums)
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if j == i:
                    continue
                else:
                    product *= nums[j]
            answer[i] = product
        return answer 