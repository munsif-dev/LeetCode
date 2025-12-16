class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dup = missing = -1
        mid_vec = [0] * (n+1)
        for num in nums:
            mid_vec[num] += 1

        for i in range(1, len(mid_vec)):
            if mid_vec[i] == 2:
                dup = i
            elif mid_vec[i] == 0:
                missing = i
        
        return dup, missing



        


        

        