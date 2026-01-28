class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        arrSize = len(arr)
        hashMap = defaultdict(int)

        for num in arr:
            hashMap[num] += 1

        maxHeap = []

        for key in hashMap:
            heappush(maxHeap, -hashMap[key])

        setSize = 0
        currSize = arrSize

        while currSize > arrSize // 2:
            currMostFreq = -heappop(maxHeap)
            currSize -= currMostFreq
            setSize += 1

        return setSize