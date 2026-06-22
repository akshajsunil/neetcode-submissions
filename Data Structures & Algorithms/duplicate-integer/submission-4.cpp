class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int,int> m;
        for(auto i :nums)
        {
            if(m.find(i)!=m.end())
            return 1;
            m[i]=i;
        }
        return 0;
        
    }
};