class Solution:
    def leaders(self, nums):
        ans = []
        n = len(nums)
        maxi = nums[-1]
        ans.append(maxi)

        for i in range(len(nums) - 1,-1,-1):
            if nums[i] > maxi:
                ans.append(nums[i])
            maxi = max(maxi,nums[i])

        ans = ans[::-1]
        return ans
