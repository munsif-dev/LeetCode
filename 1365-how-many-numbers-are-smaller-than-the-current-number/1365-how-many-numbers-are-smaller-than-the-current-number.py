class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [None] * n
        for i in range(n):
            count = 0
            for j in range(n):
                if (i != j and nums[j] < nums[i]):
                    count += 1
            out[i] = count
        return out
