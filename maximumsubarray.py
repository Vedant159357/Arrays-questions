class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = -sys.maxsize - 1
        
        summ = 0  # this gets reset to 0 everytime the sum in iteration becomes negative

        for i in  range(len(nums)):
            summ = summ + nums[i]

            if summ > maxi:
                maxi = summ

            if summ < 0:
                summ = 0

        return maxi
