class Solution:
    def check(self, nums: List[int]) -> bool:
        rotate = 0
        for i in range(len(nums)-1):
            if nums[i+1] < nums[i]:
                rotate += 1
        if rotate > 1:
            return False
        elif rotate == 1:
            if nums[len(nums)-1] <= nums[0]:
                return True
            else:
                return False
        else:
            return True
