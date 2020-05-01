class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        map<int, int> m;
        int n = 0;
        m.insert({0,-1});
        int maxl = 0, count = 0;
        for(int i = 0; i<nums.size(); i++){
            if(nums[i]==1)
                n = 1;
            else
                n = -1;
            count += n;
            if(m.find(count)!=m.end()) {
                maxl = max(maxl, i - m.find(count)->second);
            } else {
                m.insert({count, i});
            }
        }
        return maxl;
    }
};