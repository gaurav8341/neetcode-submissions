class Solution:
    def isTrionic(self, num: List[int]) -> bool:

        # order = []

        # while order != :
            # if 
        # prev = num[0]
        # for i in range(1,len(num)):
        #     latest_ord = order[-1] if order else ''
        #     if prev < num[i] and latest_ord!= 'i':
        #         order.append('i')

        #     elif prev > num[i] and latest_ord != 'd':
        #         order.append('d')
        #     else:
        #         # do not increment prev
        #         continue
        #     prev = num[i]

        # if order == ['i', 'd', 'i']:
        #     return True
        # return False
        diff = []
        p, q = 0, None
        # in diff aray 0--p-1 everything should be +ve 
        # p --> q-1 -ve 
        # q -- n +ve
        # trionic_pass = 0
        for i in range(1, len(num)):
            dif = num[i] - num[i-1]
            diff.append(dif)
            if dif > 0 and q == None:
                p += 1
            elif dif < 0 and p > 0:
                q = i
            # else:
                # return False

        print(p, q, diff)
        if q == None or p == 0 or p == q or q == len(num) - 1:
            return False
            
        for d in diff[0: p]:
            if d <= 0:
                return False
        
        for d in diff[p: q]:
            if d >= 0:
                return False

        print(diff[q:])
        for d in diff[q:]:
            if d <= 0:
                return False

        return True
        #     # if dif > 0:
        #     #     # incresing
        #     #     if trionic_pass == 0 or trionic_pass == 2:
        #     #         trionic_pass += 1
        #     # elif dif < 0:
        #     #     if trionic_pass == 1:
        #     #         trionic_pass += 1
        #     # else:
        #     #     pass
        # mode = 'i'
        # cnt = 0
        # idx = 0
        # # print( diff)
        # if len(diff) < 3:
        #     return False
        # while idx < len(diff):
        #     # if mode == i then cny must be 0 or 2
            
        #     if mode == 'i':
        #         # if cnt != 0 or cnt != 2:
        #         #     return False
        #         # # look for this mode
        #         if diff[idx] < 0:
        #             mode = 'd'
        #             cnt += 1
        #         # idx += 1
        #     elif mode == 'd':
        #         # if cnt != 1:
        #         #     return False
        #         if diff[idx] > 0:
        #             cnt += 1
        #             mode = 'i'
        #     idx += 1
        # print(cnt, mode)
        # if cnt == 2 and mode == 'i':
        #     return True
        # return False
                
        