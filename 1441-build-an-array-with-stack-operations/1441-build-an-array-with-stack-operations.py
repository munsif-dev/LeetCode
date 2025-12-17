class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:

        i = 1
        j = 0
        out = []
        while (i <= n and j < len(target)):
            if i == target[j]:
                j += 1
                i += 1
                out.append("Push")
            else:
                i += 1
                out.append("Push")
                out.append("Pop")
        return out