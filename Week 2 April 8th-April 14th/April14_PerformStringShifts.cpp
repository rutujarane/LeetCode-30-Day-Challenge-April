class Solution {
public:
    string stringShift(string s, vector<vector<int>>& shift) {
        int d = 0;
        for(int i=0; i<shift.size(); i++){
            if(shift[i][0]==0){
                d += shift[i][1];
            }
            else{
                d -= shift[i][1];
            }
        }
        // cout<< s << " " << d << " " << s.size() << endl;
        if(d>0){
            s = s.substr(d%s.size()) + s.substr(0,d%s.size());
        }
        else if(d<0){
            if(-d>s.size()){
                d = -(-d%s.size());
            }
            s = s.substr(s.size()+d) + s.substr(0,s.size()+d);
        }
        return s;
    }
};