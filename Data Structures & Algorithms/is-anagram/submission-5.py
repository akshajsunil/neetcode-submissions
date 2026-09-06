class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1=len(s)
        t1=len(t)
        if s1 != t1:
            return False
        arr = [0]*26
        for i in range(s1):
            arr[ord(s[i])-ord("a")]+=1
            arr[ord(t[i])-ord("a")]-=1
        for i in arr:
            if i!=0:
                return False


        return True
            

        

        