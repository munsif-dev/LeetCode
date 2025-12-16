class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        expected_sum = n * (n+1) /2
        array_sum = sum(nums)
        uniq_sum = sum(set(nums))
        return int(array_sum - uniq_sum), int(expected_sum - uniq_sum)



        


        

        