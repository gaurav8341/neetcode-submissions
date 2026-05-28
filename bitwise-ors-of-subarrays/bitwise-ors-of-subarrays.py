class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        # Get number of distinct bitwise ors for all subarrays
        # 
        # bri]ute force go through all combinataions n^2

        # dynamic approach

        current_ors = set()
        result_ors = set()

        for x in arr:
            # next_ors = set()
            next_ors = {x|y for y in current_ors}
            # next_ors = set(next_ors)
            next_ors.add(x)

            result_ors.update(next_ors)

            current_ors = next_ors

        return len(result_ors)
