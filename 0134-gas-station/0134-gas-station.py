class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        if sum(cost) > sum(gas):
            return -1
        tank = 0
        start = 0
        for i in range(n):
            if tank + gas[i] > cost[i]:
                tank = tank + gas[i] - cost[i]
            else:
                start += 1
        
        return start
            

