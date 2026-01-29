class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)
        ans = float("inf")

        while left <= right:
            mid = (left + right) // 2
            numArrs = 1
            currSum = 0

            for num in nums:
                currSum += num

                if currSum > mid:
                    numArrs += 1
                    currSum = num

            if numArrs <= k:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans