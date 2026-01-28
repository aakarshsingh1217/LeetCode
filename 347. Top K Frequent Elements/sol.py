class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = defaultdict(int)

        for elem in nums:
            hashMap[elem] += 1

        heap = [(-v, k) for k, v in hashMap.items()]
        heapify(heap)
        ans = []
        i = 0

        while len(heap) > 0 and i < k:
            ans.append(heappop(heap)[1])
            i += 1

        return ans