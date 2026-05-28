class TreiNode:
    def __init__(self):
        # self.val = None
        self.children = {}
        self.is_complete = False # this is true only if its leaf node


class Trie:

    def __init__(self):
        # self.val = None
        # self.children = 
        self.root = TreiNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TreiNode()
            cur = cur.children[c]
        cur.is_complete = True


    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False
        return cur.is_complete

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False
        return True
        