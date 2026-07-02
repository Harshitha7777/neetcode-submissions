class Solution:
    def isValid(self, s: str) -> bool:
        mapp = {')':'(','}':'{',']':'['}
        x = []
        for i in s:
            if(i not in mapp):
                x.append(i)
            else:
                if len(x) == 0:
                    return False
                if(x[-1] != mapp[i]):
                    return False
                x.pop()
        return len(x) == 0

        