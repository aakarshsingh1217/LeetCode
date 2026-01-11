def maxNumberOfBalloons(self, text: str) -> int:
    bCount = aCount = lCount = oCount = nCount = 0

    for char in text:
        if char == "b":
            bCount += 1
        elif char == "a":
            aCount += 1
        elif char == "l":
            lCount += 1
        elif char == "o":
            oCount += 1
        elif char == "n":
            nCount += 1

    if (lCount > 0 and oCount > 0):
        lCount //= 2
        oCount //= 2

    return min(bCount, aCount, lCount, oCount, nCount)