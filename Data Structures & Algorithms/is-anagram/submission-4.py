class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        a = {}
        b = {}
        for i in range(len(s)):
            a[s[i]] = s.count(s[i])
            b[t[i]] = t.count(t[i])
        return a == b

        