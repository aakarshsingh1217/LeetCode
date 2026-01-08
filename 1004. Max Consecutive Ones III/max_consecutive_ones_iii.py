def longestOnes(nums: list[int], k: int) -> int:
    left = numZeros = ans = 0
    
    for right in range(len(nums)):
        if nums[right] == 0:
            numZeros += 1
            
        while numZeros > k:
            if nums[left] == 0:
                numZeros -= 1
            
            left += 1
            
        ans = max(ans, right - left + 1)
        
    return ans

input = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(f"Final sol: {longestOnes(input, k)}")

"""
- Complexity analysis:
  - Time compl.: O(N), where N is num. elems. in arr. Worst
  case we might end up visiting every elem. of array twice,
  once by left pointer and once by right ptr.
  - Space compl: O(1) (no extra space used).
"""