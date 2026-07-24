class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        i = 0
        j = len(heights) - 1
        while(i<j):
            a = (j-i) * min(heights[i], heights[j])
            if(a > result):
                result = a
            if(heights[i] < heights[j]):
                i += 1
            elif(heights[i] > heights[j]):
                j -= 1
            else:
                i += 1
                j -= 1
        return result

        