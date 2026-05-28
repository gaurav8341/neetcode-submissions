class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ascii_sum_map = {} # ascii_sum -> [words]

        for s in strs:
            ascii_sum = self.get_ascii(s)
            ascii_sum_list = ascii_sum_map.get(ascii_sum, list())
            ascii_sum_list.append(s)
            ascii_sum_map[ascii_sum] = ascii_sum_list

        return list(ascii_sum_map.values()) 

    def get_ascii(self, s: str) -> int:
        ascii_sum = 0
        for ch in s: 
            ascii_sum += ord(ch)
        
        return ascii_sum