class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        heapify(asteroids)

        while mass > 0 and asteroids:
            nextElem = heappop(asteroids)

            if mass >= nextElem:
                mass += nextElem
            else:
                mass -= nextElem

        return mass >= 0