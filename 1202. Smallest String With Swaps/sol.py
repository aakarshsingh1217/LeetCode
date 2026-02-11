from collections import defaultdict

def smallestStringWithSwaps(s: str, pairs: list[list[int]]) -> str:
    n = len(s)

    adj = defaultdict(list)

    for a, b in pairs:
        adj[a].append(b)
        adj[b].append(a)

    visited = set()
    s = list(s)

    def dfs(vertex, indices, characters):
        visited.add(vertex)
        indices.append(vertex)
        characters.append(s[vertex])

        for nei in adj[vertex]:
            if nei not in visited:
                dfs(nei, indices, characters)

    for i in range(n):
        if i not in visited:
            indices = []
            characters = []
            dfs(i, indices, characters)

            indices.sort()
            characters.sort()

        for i in range(len(indices)):
            s[indices[i]] = characters[i]

    return "".join(s)