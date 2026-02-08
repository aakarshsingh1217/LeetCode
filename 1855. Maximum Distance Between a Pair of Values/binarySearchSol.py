def maxDistance(nums1: list[int], nums2: list[int]) -> int:
    m, n = len(nums1), len(nums2)
    res = 0

    # Reverse nums2 so it becomes non-decreasing
    nums2.reverse()

    for i in range(m):
        left = 0
        right = n - 1
        pos = n   # leftmost index where nums2[pos] >= nums1[i]

        while left <= right:
            mid = (left + right) // 2

            if nums2[mid] >= nums1[i]:
                pos = mid
                right = mid - 1
            else:
                left = mid + 1

        # If such a position exists
        if pos < n:
            # Map back to original index in nums2
            j = n - 1 - pos

            # Check index constraint
            if j >= i:
                res = max(res, j - i)

    return res