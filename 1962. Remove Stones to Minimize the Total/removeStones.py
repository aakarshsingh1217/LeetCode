class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        nums = [-num for num in piles]
        
        heapify(nums)

        for _ in range(k):
            maxNum = abs(heappop(nums))
            maxNum -= (maxNum // 2)
            heappush(nums, -maxNum)

        return -sum(nums)