class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        order = sorted(arr, reverse=True)
        diff = order[0] - order[1]
        for i in range(len(order)-1):
            if order[i] - order[i+1] != diff:
                return False
        return True