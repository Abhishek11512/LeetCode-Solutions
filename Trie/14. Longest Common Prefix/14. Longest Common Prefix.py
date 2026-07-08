class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        strs.sort()
        f, l = strs[0],strs[-1]

        for i in range(len(f)):
            if i >= len(l) or f[i] != l[i]:
                return f[:i]

        return f