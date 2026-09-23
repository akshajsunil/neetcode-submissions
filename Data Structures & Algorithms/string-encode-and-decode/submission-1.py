class Solution:

    def encode(self, strs: List[str]) -> str:

        s =""
        for i in strs:
            
            s+=i
            s+="~"
        return s
    def decode(self, s: str) -> List[str]:
        p =  s.split("~")
        p = p[:-1]
        return p
