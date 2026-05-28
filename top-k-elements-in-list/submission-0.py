class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count_map = dict()
        result = set()

        def pop_add(result, count_map, n):
            n_count, least_num = count_map[n], None
            new_result = result.copy()
            for no in result:
                if count_map[no] < n_count:
                    new_result.remove(no)
                    new_result.add(n)

            return new_result

        for n in nums:
            count_map[n] = count_map.get(n, 0) + 1
            if n in result:
                continue
            if len(result) < k:
                result.add(n)
            elif len(result) == k:
                result = pop_add(result, count_map, n)
      
        return list(result)
            