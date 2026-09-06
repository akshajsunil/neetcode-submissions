class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1=len(s)
        t1=len(t)
        if s1 != t1:
            return False
        d1 = {}
        
        for i in s:
            if i in d1:
                d1[i]+=1
            else:
                d1[i]=1
        for i in t:
            if i in d1:
                d1[i]-=1
            else:
                return False
        for i in d1:
            if d1[i]>0:
                return False
        return True
            

        

        