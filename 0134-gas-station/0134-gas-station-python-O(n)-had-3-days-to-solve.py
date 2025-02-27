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
            tank = tank + gas[i] - cost[i]
            if tank < 0:
                tank = 0
                start = i + 1
        
        return start
            

