class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res = []
        dictt = Counter(nums)
        for key,value in dictt.items():
            if value > 1:
                res.append(key)

        return res


# Cunter(nums) is a special dictionary subclass provided by Python's collections module.
#When Counter(nums) is called, it takes the input list nums and returns a dictionary-like object where:
#The keys are the unique elements from nums.
#The values are the counts (frequencies) of how many times each element appears in nums.
