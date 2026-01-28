class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        numApples = 0
        currTotal = 0

        for appleWeight in weight:
            if currTotal + appleWeight <= 5000:
                currTotal += appleWeight
                numApples += 1
            else:
                break

        return numApples