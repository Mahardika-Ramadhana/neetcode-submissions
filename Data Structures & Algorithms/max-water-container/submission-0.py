class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        
        i = 0
        j = len(heights) - 1

        while i < j:
            current = (j - i) * min(heights[i], heights[j])
            if ans < current:
                ans = current
            else:
                if (heights[i] > heights[j]):
                    j -= 1
                else:
                    i += 1

        return ans
