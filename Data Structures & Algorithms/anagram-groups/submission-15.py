class Solution:
    def findhash(self,strs):
        t=0
        for i in strs:
            t+=(ord(i)-ord("a")+4543)**4
        return t
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in strs:
            t=self.findhash(i)
            #print(t)
            if t not in dic :
                dic[t] = [i]
            else:
                dic[t].append(i)
        l =[]
        for i in dic:
            l.append(dic[i])
        return l

        