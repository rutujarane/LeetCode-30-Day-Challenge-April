class Solution {
public:
    int countElements(vector<int>& arr) {
        map<int,int> s;
        for(int i=0; i<arr.size(); i++){
            if(s.find(arr[i])!=s.end())
                s[arr[i]]++;
            else
                s[arr[i]] = 1;
        }
        int count = 0;
        for(auto itr=s.begin(); itr!=s.end(); itr++){
            // cout<<*itr<<endl;
            if(s.find((itr->first)+1)!=s.end()){
                count+=itr->second;
            }
        }
        return count;
    }
};