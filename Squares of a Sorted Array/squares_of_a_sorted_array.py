class Solution:
    def sortedSquared(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1

        for i in range(n - 1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1

            result[i] = square * square

        return result
    
"""
Time: O(n) (for loop going through all elems.)
Space: O(n) (output array size n)
"""