class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        l = []
        for i in range(len(nums)):
            if(nums[i] not in s):
                diff = target - nums[i]
                s[diff] = i
            else:
                return [s[nums[i]],i]

        