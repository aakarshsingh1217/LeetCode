class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans = []

        def backtrack(numList: list[int], currNum: int):
            if len(numList) == n:
                ans.append(int("".join(map(str, numList))))
                return

            next1 = currNum + k
            if next1 <= 9:
                numList.append(next1)
                backtrack(numList, next1)
                numList.pop()

            # prevent duplicate path when k == 0
            next2 = currNum - k
            if k != 0 and next2 >= 0:
                numList.append(next2)
                backtrack(numList, next2)
                numList.pop()

        for i in range(1, 10):
            backtrack([i], i)

        return ans