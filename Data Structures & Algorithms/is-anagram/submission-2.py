class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1=len(s)
        t1=len(t)
        if s1 != t1:
            return False
        d1 = {}
        d2 = {}
        for i in s:
            if i in d1:
                d1[i]+=1
            else:
                d1[i]=1
        for j in t:
            if j in d2:
                d2[j]+=1
            else:
                d2[j]=1
        for i in d1:
            if i not in d2 or d2[i]!=d1[i]:
                return False
        return True
            

        

        