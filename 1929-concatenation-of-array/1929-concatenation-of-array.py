class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [None] * (n*2)
        i = 0
        j = 0
        while i < len(ans):
            ans[i] = nums[j]
            i += 1
            j = (j + 1)%n
        
        return ans


        

        