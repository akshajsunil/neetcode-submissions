class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.length()!=t.length())
        return 0;
        map<char ,int> m1,m2;
        for(int i;i<s.length();i++)
        {
            m1[s[i]]++;
            m2[t[i]]++;
        }
        if(m1==m2)
        return 1;
        return 0;
        
    }
};
