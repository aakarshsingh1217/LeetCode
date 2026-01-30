class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node: int, curr: list[int]):
            if node == len(graph) - 1:
                ans.append(curr[:])

                return

            for neighbour in graph[node]:
                curr.append(neighbour)
                dfs(neighbour, curr)
                curr.pop()

        ans = []
        dfs(0, [0])

        return ans