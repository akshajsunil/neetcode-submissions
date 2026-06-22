class Solution:
    def isValid(self, s: str) -> bool:
        if (len(s)%2==1):
            return False
        dict_c = {'(':')','{': '}', '[' :']'}
        st=[]
        for i in s:
            if i in dict_c.keys():
                st.append(i)
            if i in dict_c.values():
                if not st:
                    return False
                if  dict_c[st.pop()]!=i:
                    return False
        if not st:
            return True
        return False
        