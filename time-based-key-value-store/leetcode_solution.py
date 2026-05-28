class TimeMap:

    def __init__(self):
        self.kvmap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.kvmap.keys():
            self.kvmap[key] = []
        # if timestamp not in self.kvmap[key].keys():
        #     self.kvmap[key][timestamp] = None
        self.kvmap[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        v = self.kvmap.get(key, [])
        l, r = 0, len(v)-1
        while l <= r:
            m = int((l+r) // 2)

            if v[m][1] <= timestamp:
                res =  v[m][0]
                l = m + 1
            elif v[m][1] > timestamp:
                r = m - 1
        return res
