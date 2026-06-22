class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> m,n;
        int k=0;
        for(auto i: nums)
        {
            if(m[target-i]!=0)
            return {n[target-i],k};
            m[i]++;
            n[i]=k;
            k++;
            
        }
        
    }
};
