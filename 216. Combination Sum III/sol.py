class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def backtrack(currNum: int, currSum: int, numList: list[int], numDigits: int):
            if currSum == n and numDigits == k:
                ans.append(numList[:])

                return

            for i in range(currNum, 10):
                if currSum + i <= n and numDigits <= k:
                    numList.append(i)
                    backtrack(i + 1, currSum + i, numList, numDigits + 1)
                    numList.pop()

        for i in range(1, 10):
            backtrack(i + 1, i, [ i ], 1)

        return ans