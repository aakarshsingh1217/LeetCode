class Solution:
    def maximum69Number (self, num: int) -> int:
        digitsList = [int(digit) for digit in str(num)]
        digitsListLen = len(digitsList)
        foundFirstSix = False
        i = 0

        while not foundFirstSix and i < digitsListLen:
            if digitsList[i] == 6:
                break

            i += 1

        if i < digitsListLen and digitsList[i] == 6:
            digitsList[i] = 9

        numberStr = "".join(str(digit) for digit in digitsList)

        return int(numberStr)