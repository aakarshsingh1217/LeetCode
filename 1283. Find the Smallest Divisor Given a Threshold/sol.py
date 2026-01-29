class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)

        def check(divisor: int):
            sumDividedNums = 0

            for num in nums:
                sumDividedNums += ceil(num / divisor)

            return sumDividedNums <= threshold

        while left <= right:
            mid = (left + right) // 2

            if check(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left