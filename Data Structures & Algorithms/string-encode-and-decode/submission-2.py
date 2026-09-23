class Solution:

    def encode(self, strs: List[str]) -> str:

        s =""
        for i in strs:
            
            s+=str(len(i))+"~"+i
        
        return s
    def decode(self, s: str) -> List[str]:
        i=0
        j=0
        ans =[]
        while i<len(s):
            if s[i]=="~":
                u = int(s[j:i])
                st = s[i+1:i+u+1]
                ans.append(st)
                j=u+i+1
                i=u+1+i
                print(u)
                print(st)
            i+=1
        return ans

