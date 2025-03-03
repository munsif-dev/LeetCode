class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        candy = n

        forward = [0] * n
        backward = [0] * n

        for i in range(1,n):
            if ratings[i] > ratings[i-1]:
                forward[i] = forward[i-1] + 1
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                backward[i] = backward[i+1] + 1
        for i in range(n):
            candy += max(forward[i] , backward[i])
        
        return candy
