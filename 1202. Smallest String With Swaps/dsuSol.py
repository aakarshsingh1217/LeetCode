from collections import defaultdict

class UnionFind:
    def __init__(self, size: int):
        self.root = [node for node in range(size)]
        self.rank = [1] * size

    def find(self, x: int) -> int:
        if x == self.root[x]:
            return x
        
        self.root[x] = self.find(self.root[x])

        return self.root[x]
    
    def union(self, x: int, y: int):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootY] > self.rank[rootX]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

def smallestStringWithSwaps(s: str, pairs: list[list[int]]) -> str:
    uf = UnionFind(len(s))
    rootToComponent = defaultdict(list)
    strList = list(s)

    for a, b in pairs:
        uf.union(a, b)

    for i in range(len(s)):
        rootToComponent[uf.find(i)].append(i)

    for componentList in rootToComponent.values():
        chars = []
        indices = []

        for idx in componentList:
            chars.append(strList[idx])
            indices.append(idx)

        chars.sort()
        indices.sort()

        for i in range(len(indices)):
            strList[indices[i]] = chars[i]

    return "".join(strList)