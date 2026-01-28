class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            euclidDist = (x - 0) ** 2 + (y - 0) ** 2
            heappush(heap, (-euclidDist, (x, y)))

            if len(heap) > k:
                heappop(heap)

        return [[heapElem[1][0], heapElem[1][1]] for heapElem in heap]