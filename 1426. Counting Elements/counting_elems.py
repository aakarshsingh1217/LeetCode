def countElements(self, arr: list[int]) -> int:
    arr_set = set(arr)
    ans = 0

    for num in arr:
        if num + 1 in arr_set:
            ans += 1

    return ans