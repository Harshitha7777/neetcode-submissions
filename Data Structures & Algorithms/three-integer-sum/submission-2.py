class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)-2):
            if(i > 0 and nums[i] == nums[i-1]):
                continue
            else:
                t = -nums[i]
                j, k = i+1, len(nums)-1
                while(j < k):
                    d = nums[j] + nums[k]
                    if(d == t):
                        result.append([nums[i], nums[j], nums[k]])
                        j += 1
                        k -= 1
                        while(j<k and nums[j] == nums[j-1]):
                            j += 1
                        while(j<k and nums[k] == nums[k+1]):
                            k -= 1
                    elif(d < t):
                        j += 1
                    else:
                        k -= 1
            
        return result

        