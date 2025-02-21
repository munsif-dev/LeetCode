import random
class RandomizedSet(object):

    def __init__(self):
        global list1
        list1 = []
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in list1:
            return False
        else:
            list1.append(val)
            return True
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in list1:
            list1.remove(val)
            return True
        else:
            return False

    def getRandom(self):
        """
        :rtype: int
        """
        r_n = random.randrange(len(list1))
        return list1[r_n]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()