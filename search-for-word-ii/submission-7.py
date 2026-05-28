class TrieNode:
    def __init__(self ):#prefix:str='', node_char:str=None):
        self.children = {}
        self.is_complete = False
        # self.word = prefix + node_char
        # prefix is the word of parent
        # node_char is char of the current word
    
    def __str__(self):
        return "-".join(self.children.keys()) + "#" + self.is_complete

class Solution:

    # def addWords(self, words:List[str]):
        
    
    def find(self, board:List[List[str]]) ->List[str]:
        ROWS, COLS = len(board), len(board[0])

        res, visit = set(), set()
        #The same cell may not be used more than once in a word.
        # here within word a single cell is not repeated. but across words it may be repeated
        # i, j = 0, 0

        def dfs(r, c, node, word):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS \
            or (r, c) in visit or board[r][c] not in node.children:
                return

            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.is_complete:
                # print(node.is_complete, board[r][c], r, c)
                res.add(word)

            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c-1, node, word)
            dfs(r, c+1, node, word)  
            visit.remove((r,c))

        cur = self.root
        for r in range(ROWS):
            for c in range(COLS):
                # no we will do dfs 
                dfs(r, c, self.root, '')
        
        return list(res)
        

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 2d grid  and words return all words, present in grid
        # saame cell cant be used more than once

        # if we build trie from word it will be

        root = TrieNode()
        # add words in Trie

        for word in words:
            cur = root
            for w in word:
                if w not in cur.children:
                    cur.children[w] = TrieNode()
                cur = cur.children[w]
            cur.is_complete = True

        # now find word in metrix

        ROWS, COLS = len(board), len(board[0])

        res, visit = set(), set()
        #The same cell may not be used more than once in a word.
        # here within word a single cell is not repeated. but across words it may be repeated
        # i, j = 0, 0

        def dfs(r, c, node, word):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS \
            or (r, c) in visit or board[r][c] not in node.children:
                return

            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.is_complete:
                # print(node.is_complete, board[r][c], r, c)
                res.add(word)

            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c-1, node, word)
            dfs(r, c+1, node, word)  
            visit.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                # no we will do dfs 
                dfs(r, c, root, '')
        
        return list(res)
        # return self.find(board)

