class Solution:
    def minOperations(self, s: str) -> int:
        res1 = 0  # target 010101...
        res2 = 0  # target 101010...

        for i in range(len(s)):
            expected1 = "0" if i % 2 == 0 else "1"
            expected2 = "1" if i % 2 == 0 else "0"

            if s[i] != expected1:
                res1 += 1

            if s[i] != expected2:
                res2 += 1

        return min(res1, res2)
