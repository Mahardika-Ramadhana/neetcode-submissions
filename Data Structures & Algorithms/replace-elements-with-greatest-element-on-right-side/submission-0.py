class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = []
        m = 0
        i, j = 0, len(arr)
        while i < len(arr):
            if i == 0:
                ans.append(-1)
            else:
                m = max(arr[j], m)
                ans.append(m)
            i += 1
            j -= 1
        
        return ans[::-1]
