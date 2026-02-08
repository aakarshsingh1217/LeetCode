def firstBadVersion(n: int) -> int:
    left = 1
    right = n

    while left < right:
        mid = (left + right) // 2

        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1

    return left

def isBadVersion(val: int) -> bool:
    pass