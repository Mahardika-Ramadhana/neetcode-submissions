class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        for i in range(n - m + 1):
            j = 0
            while j < len(needle):
                if haystack[i + j] != needle[j]:
                    break
                else:
                    j += 1
            if j == m:
                return i
        return -1