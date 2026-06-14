class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        for value in hashmap.values():
            if value > 1:
                return True
        
        return False
