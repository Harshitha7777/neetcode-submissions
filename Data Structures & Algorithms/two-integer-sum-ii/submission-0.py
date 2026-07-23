class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s = {}
        for i, num in enumerate(numbers):
            if num in s:
                return[s[num]+1, i+1]
            else:
                d = target - num
                s[d] = i
        