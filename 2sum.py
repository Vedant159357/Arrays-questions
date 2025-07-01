class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i,num in enumerate(nums): #enumerate() returns index as well as element of a list
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]

            hashmap[num] = i

        return []
