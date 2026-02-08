"""
- Focus on two adjacent elems. nums1[i] and nums1[i'] and
assume that we've found insertion pos. of them as j
and j'.
- Since i < i' and nums1 is in descending order, therefore
nums1[i] >= nums1[i'], leads to nums2[j] >= nums2[j'].
  - nums1 [* i i' * * * * *]
      nums1[j] >= nums1[j'] -
                            |
                            |
    nums2 [* * j * j' *]    |
      nums2[i] >= nums2[i']↩
  - Implies that as we traverse over nums1, the insertion
  pos j found each time is in ascending order!
  - Therefore, we don't need to use binary search to find
  every insertion pos.
  - Instead, we can use another pointer referring to the
  insertion pos. to nums2, during the iteration over
  nums1, the pointer to nums2 will only move to the
  right.
  - Thus, we no longer need repeatedly binary search
  over nums2!

- E.g.:
  - nums1 [55, 30, 5, 4, 2]     Start with i = 0 and j = 0.
           p1                   For each j, we find the
    nums2 [100, 20, 10, 10, 5]  first p1 that makes
           p2                   nums1[p1] <= nums2[p2].
"""