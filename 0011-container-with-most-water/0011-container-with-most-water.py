class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        area = 0


        while(l<r):
            cur_area = ( r - l ) * min(height[r], height[l])
            if cur_area > area:
                area = cur_area
                if height[l] >= height[r]:
                    r -= 1
                else:
                    l += 1
            else:
                if height[l] >= height[r]:
                    r -= 1
                else:
                    l += 1
        return area

        