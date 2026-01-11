from collections import defaultdict

def largestUniqueNumber(nums: list[int]) -> int:
    num_counts = defaultdict(int)

    for num in nums:
        num_counts[num] += 1

    best = -1

    for key in num_counts:
        if num_counts[key] == 1 and key > best:
            best = key

    return best