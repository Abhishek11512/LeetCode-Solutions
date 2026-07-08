
class Solution:
    def pivotInteger(self, n: int) -> int:
        T_sum = (n*(n+1) // 2)
        P = T_sum ** 0.5

        if P % 1 == 0:
            return int(P)
    
        return -1