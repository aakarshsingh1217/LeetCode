class Solution:
    def validPath(self, n: int, edges: List[List[int]],
                  source: int, destination: int) -> bool:
        hashmap = defaultdict(list)

        for x, y in edges:
            hashmap[x].append(y)
            hashmap[y].append(x)

        seen = set([source])

        def dfs(node: int) -> bool:
            if node == destination:
                return True

            for neighbour in hashmap[node]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    if dfs(neighbour):
                        return True
            return False

        return dfs(source)