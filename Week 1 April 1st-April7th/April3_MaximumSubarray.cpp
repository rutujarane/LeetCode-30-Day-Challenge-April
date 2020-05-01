class Solution {
public:
    int maxSubArray(vector<int>& nums) {
 
        int max_so_far = INT_MIN, max_ending_here = 0; 

        for (int i = 0; i < nums.size(); i++) 
        { 
            // cout<<"i "<<i<<" "<<nums[i]<<endl;
            // cout<<max_ending_here<<" "<<max_so_far<<endl;
            max_ending_here = max_ending_here + nums[i]; 
            // cout<<"after"<<max_ending_here<<endl;
            if (max_so_far < max_ending_here) 
                max_so_far = max_ending_here; 
            if (max_ending_here < 0) 
                max_ending_here = 0; 
            // cout<<"AA"<<max_ending_here<<" "<<max_so_far<<endl;
        } 
        return max_so_far; 
    }
};