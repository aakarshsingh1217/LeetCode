from collections import deque

class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans = []

        for i in range(len(nums1)):
            monotonic_decr = deque([nums1[i]])
            j = 0

            while nums2[j] != nums1[i]:
                j += 1

            for k in range(j + 1, len(nums2)):
                while monotonic_decr and monotonic_decr[-1] < nums2[k]:
                    monotonic_decr.pop()
                
                monotonic_decr.append(nums2[k])

                if monotonic_decr and monotonic_decr[0] > nums1[i]:
                    break

            if monotonic_decr[0] == nums1[i]:
                ans.append(-1)
            else:
                ans.append(monotonic_decr.popleft())

        return ans