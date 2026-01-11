from collections import defaultdict

def numJewelsInStones(self, jewels: str, stones: str) -> int:
    stones_count = defaultdict(int)

    for ch in stones:
        stones_count[ch] += 1

    ans = 0

    for ch in jewels:
        if ch in stones_count:
            ans += stones_count[ch]

    return ans