class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        restricted_set = set()

        for node in restricted:
            restricted_set.add(node)

        graph = defaultdict(list)

        for x, y in edges:
            if x not in restricted_set and y not in restricted_set:
                graph[x].append(y)
                graph[y].append(x)

        seen = set([0])

        def dfs(node: int):
            nonlocal seen
            num_nodes = 1

            for neighbour in graph[node]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    num_nodes += dfs(neighbour)

            return num_nodes

        return dfs(0)