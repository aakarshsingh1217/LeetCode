class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numDict = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"]
        }
        digitsLen = len(digits)

        def backtrack(curr: list[str], currDigitIndex: int):
            if len(curr) == digitsLen:
                ans.append("".join(curr))

                return

            for char in numDict[listOfInts[currDigitIndex]]:
                curr.append(char)
                backtrack(curr, currDigitIndex + 1)
                curr.pop()

        listOfInts = [int(num) for num in digits]
        ans = []
        backtrack([], 0)

        return ans