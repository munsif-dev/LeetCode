class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        n = len(citations)
        for i in range(0,n):
            if i + citations[i] >= (n-1):
                if  citations[i] >= n-i :
                    return n-i
                else:
                    return citations[i]

        



