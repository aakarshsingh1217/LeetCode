def minStartValue(self, nums: list[int]) -> int:
    minVal = 0
    total = 0

    for num in nums:
        total += num
        minVal = min(minVal, total)

    return 1 - minVal