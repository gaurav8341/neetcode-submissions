from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # We need to first create a adj list for the dict.
        # instead of traditional approach of forming it 
        # we will find pattern in words and use at keys in adj list.

        # m = no. of words
        # n = len of each word.
        if endWord not in wordList:
            return 0

        adj_list = defaultdict(list)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j+1:]
                adj_list[pattern].append(word)
        
        visit = set()
        q = deque()

        q.append(beginWord)
        visit.add(beginWord)
        res = 0

        while q:
            qlen = len(q)
            res += 1
            for _ in range(qlen):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j+1:]
                    for nei in adj_list[pattern]:
                        if nei not in visit:
                            visit.add(nei)
                            q.append(nei)

        return 0
                        

