class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        choices = ["A", "C", "G", "T"]

        def neighbours(node: str):
            neighbours = []

            for i in range(8):
                for next_char in choices:
                    if next_char != node[i]:
                        new_str = node[:i] + next_char + node[i + 1:]

                        if new_str in bank:
                            neighbours.append(new_str)

            return neighbours

        queue = deque([(startGene, 0)])
        seen = {startGene}

        while queue:
            curr_node, steps = queue.popleft()

            if curr_node == endGene:
                return steps

            for neighbour in neighbours(curr_node):
                if neighbour not in seen:
                    seen.add(neighbour)
                    queue.append((neighbour, steps + 1))

        return -1