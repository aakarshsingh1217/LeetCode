class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        seen = set()
        ans = 0

        def dfs(node):
            nonlocal seen

            for neighbour in graph[node]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    dfs(neighbour)

        for i in range(len(graph)):
            if i not in seen:
                ans += 1
                seen.add(i)
                dfs(i)

        
        return ans