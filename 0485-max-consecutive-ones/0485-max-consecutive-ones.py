class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        temp_max_count = 0
        max_cons = 0
        for num in nums:
            if num == 1:
                temp_max_count += 1
                if temp_max_count > max_cons:
                    max_cons = temp_max_count
            else:
                temp_max_count = 0
        return max_cons

        