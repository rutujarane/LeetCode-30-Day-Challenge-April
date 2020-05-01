class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        // int count = 0;
        // for(int i=0; i<nums.size(); i++){
        //     // cout<<nums[i]<<endl;
        //     if(nums[i]==0){
        //         // cout<<"del"<<endl;
        //         count++;
        //         nums.erase(nums.begin() + i);
        //         // cout<<"done"<<endl;
        //         i--;
        //     }
        // }
        // // cout<<"hi"<<endl;
        // while(count!=0){
        //     nums.push_back(0);
        //     count--;
        // }
        
        for (int lastNonZeroFoundAt = 0, cur = 0; cur < nums.size(); cur++) {
            if (nums[cur] != 0) {
                swap(nums[lastNonZeroFoundAt++], nums[cur]);
            }
        }
    }
};