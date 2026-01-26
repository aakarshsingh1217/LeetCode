class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        runningTotal = 0
        heapify(sticks)

        while len(sticks) > 1:
            smallest = heappop(sticks)
            secondSmallest = heappop(sticks)
            newNum = smallest + secondSmallest
            runningTotal += newNum
            heappush(sticks, newNum)

        return runningTotal