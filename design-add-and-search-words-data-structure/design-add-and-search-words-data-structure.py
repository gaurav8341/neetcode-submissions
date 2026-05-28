class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_complete = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_complete = True
        

    def search(self, word: str) -> bool:
        # cur = self.root
        # for c in word:
        #     if c in cur.children or c == '.':
        #         if c != '.':
        #             cur = cur.children[c]
        #         else:
        #             # here dfs and backtracking needs to be performed
                    
        #     else:
        #         return False
        # return cur.is_complete
        def dfs(i, root):
            cur = root
            # if it is . then we need to process next request anywaysif it is not then as usual

            for j in range(i, len(word)):
                if word[j] in cur.children:
                    cur = cur.children[word[j]]
                elif word[j] != '.':
                    return False
                else:
                    # character is .
                    # check all children
                    for child in cur.children.values():
                        # print(dfs(j+1, child), child, child.children.keys())
                        if dfs(j+1, child):
                            # this checked entire of remaining children
                            return True
                    return False
            print(word, cur.is_complete)
            return cur.is_complete


        return dfs(0, self.root)