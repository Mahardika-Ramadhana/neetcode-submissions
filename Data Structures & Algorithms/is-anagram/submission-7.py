class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hs = {}
        ht = {}

        for char in s:
            hs[char] = hs.get(char, 0) + 1
        for char in t:
            ht[char] = ht.get(char, 0) + 1

        return hs == ht        
