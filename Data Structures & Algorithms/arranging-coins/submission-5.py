class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        while n > 0:
            n -= i
            if n < 0:
                break
            i += 1
        return i-1
        