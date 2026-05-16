class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
#         # product = [1] * len(nums)

#         # is_zero = True if 0 in nums else False
#         # product_wo_0 = 1

#         # for num in nums:
#         #     if num != 0:
#         #         product_wo_0 *= num
        
#         # product = []
#         # for i in range(len(nums)):
#         #     if is_zero:
#         #         prod = 0 if nums[i] != 0 else int(product_wo_0)
#         #         product.append(prod)
#         #         continue
#         #     product.append(int(product_wo_0/nums[i]))
        
#         # return product

        results = [1] * (len(nums))

        for i in range(1, len(nums)):
            results[i] = results[i-1]*nums[i-1]

            # results[i] = results[i] * results[i-1]
        
        print(results)
        postfix = 1

        for i in range(len(nums)-1, -1, -1):
            results[i] *= postfix

            postfix *= nums[i]

        return results 




# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         res = [1] * (len(nums))

#         for i in range(1, len(nums)):
#             res[i] = res[i-1] * nums[i-1]
#         postfix = 1
#         for i in range(len(nums) - 1, -1, -1):
#             res[i] *= postfix
#             postfix *= nums[i]
#         return res
