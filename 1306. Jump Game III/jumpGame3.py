class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        arrLen = len(arr)
        queue = deque([start])
        seen = set()

        while queue:
            node = queue.popleft()

            if arr[node] == 0:
                return True

            if node + arr[node] < arrLen and node + arr[node] not in seen:
                seen.add(node + arr[node])                
                queue.append(node + arr[node])
            if node - arr[node] >= 0 and node - arr[node] not in seen:
                seen.add(node - arr[node])                    
                queue.append(node - arr[node])

        return False