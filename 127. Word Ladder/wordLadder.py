class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def neighbours(node: str):
            strLen = len(node)
            ans = []

            for word in wordList:
                matches = 0

                for i in range(strLen):
                    if node[i] == word[i]:
                        matches += 1
                
                if matches == strLen - 1:
                    ans.append(word)

            return ans

        queue = deque([(beginWord, 1)])
        seen = { beginWord }

        while queue:
            currWord, numWords = queue.popleft()

            if currWord == endWord:
                return numWords

            for neighbour in neighbours(currWord):
                if neighbour not in seen:
                    seen.add(neighbour)
                    queue.append((neighbour, numWords + 1))

        return 0