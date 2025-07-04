class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        posInd, negInd = 0,1
        for i in range(len(nums)):
            if nums[i] < 0:
                ans[negInd] = nums[i]
                negInd += 2

            else:
                ans[posInd] = nums[i]
                posInd += 2

        return ans
