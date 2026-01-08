class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        currSum = 0
        
        for i in range(k):
            currSum += nums[i]
            
        currAvg = currSum / k
        maxAvg = currAvg
        
        for i in range(k, len(nums)):
            currSum += nums[i]
            currSum -= nums[i - k]
            currAvg = currSum / k
            
            maxAvg = max(maxAvg, currAvg)
            
        return maxAvg
    
"""
Notes: Don't need to keep average, can just find max sum
then return maxSum / fixedSizeOfWindowVar.

Best sol:

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = 0
        for i in range(k):
            curr += nums[i]
            
        ans = curr
        
        for i in range(k, len(nums)):
            curr += nums[i] - nums[i - k]
            ans = max(ans, curr)
            
        return ans / k

Complexity analysis:
  - Time compl.: O(n), iterate over nums array of len. n once
  only.
  - Space compl.: O(1), constant extra space used.
"""