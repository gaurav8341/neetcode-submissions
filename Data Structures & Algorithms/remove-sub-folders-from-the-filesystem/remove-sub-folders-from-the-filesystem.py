class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_complete = False
    
    # def 


class Solution:

    def addWord(self, word):
        """
            we add word this will be conditional 
        """
        curr = self.root
        for c in word.split("/"):
            if not c: continue
            # if curr.is_complete:
            if c not in curr.children:
                node = TrieNode()
                curr.children[c] = node
                # curr = node
            curr = curr.children[c]
        curr.is_complete = True        

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # we have lists of folders 
        # if folder[i] is inside folder[j] then j is subfolder of a
        # Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
        # in above eg. /a/b is subfolder of /a /c/d/e is of /c/d 
        self.root = TrieNode()


        ## Trie based approach
        for f in folder:
            self.addWord(f)

        res = []
        
        def dfs(node, path):
            print(path)
            if node.is_complete:
                res.append(path)
                return
            for k, n in node.children.items():
                print(k)
                dfs(n, path+"/"+k)
        
        dfs(self.root, "")
        return res

        # lexiographical sorting if parent folder is in our set then we dont consider

        # folder.sort()
        # res = []

        # i = 0
        # # for f in folder:
        # for f in folder:
        #     if not res:
        #         res.append(f)
        #     else:
        #         prev = res[-1]
        #         if len(f) > len(prev) and f.startswith(prev) and f[len(prev)] == "/":
        #             continue
        #         else:
        #             res.append(f)

        # return res