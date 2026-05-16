class Solution:

    def encode(self, strs: List[str]) -> str:
        # return '#'.join(strs)
        encode_str = ""
        strlen = len(strs)
        # for i, s in enumerate(strs):
        #     # if i == 
        #     encode_str += s

        #     if i==strlen -1:
        #         continue
            
        #     encode_str += "#"

        for s in strs:
            encode_str += str(len(s))+'-'+s 
        
        return encode_str


    def decode(self, s: str) -> List[str]:
        # if not s:
        #     return []
        # return s.split('#')
        res = []
        # start = -1
        # for i, c in enumerate(s):
        #     if c == '#':
        #         res.append(s[start:i])
        #         start = -1
        #         continue

        #     if i == len(s) -1:
        #         res.append(s[start:i+1])
            
        #     if start == -1:
        #         start = i
        print(s)
        i=0
        while i<len(s):
            j=i
            # print()
            while s[j] != '-':
                j+=1
            length = s[i:j]
            length = int(length)
            start = j+1
            end = start+length
            res.append(s[start:end])
            print(res)
            i=end
        return res