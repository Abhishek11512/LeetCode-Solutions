class Solution:
    def romanToInt(self, s: str) -> int:
        Num_val = {"M": 1000, "D" : 500, "C" : 100, "L" : 50, "X" : 10, "V" : 5, "I" : 1}
        sum_data = 0
        n = len(s)
        for i in range(n):
            if i<n-1 and Num_val[s[i]] < Num_val[s[i+1]]:
                sum_data -= Num_val[s[i]]
            else:
                sum_data += Num_val[s[i]]
        return sum_data