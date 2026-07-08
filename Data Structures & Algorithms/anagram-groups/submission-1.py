class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        x = {}
        for i in strs:
            key = "".join(sorted(i))
            if(key not in x):
                x[key] = []
                x[key].append(i)
            else:
                x[key].append(i)
        result = []
        for i in x:
            result.append(x[i])
        return result