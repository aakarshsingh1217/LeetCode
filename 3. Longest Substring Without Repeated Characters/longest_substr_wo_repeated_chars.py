def lengthOfLongestSubstring(s: str) -> int:
    n = len(s)
    ans = 0

    # charToNextIndex stores index after curr. char.
    charToNextIndex = {}
    i = 0

    # try to extend range [i, j]
    for j in range(n):
        if s[j] in charToNextIndex:
            i = max(charToNextIndex[s[j]], i)

        ans = max(ans, j - i + 1)
        charToNextIndex[s[j]] = j + 1

    return ans