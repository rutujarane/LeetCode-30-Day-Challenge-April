class Solution {
public:
    bool isHappy(int n) {
        int ne=0,r=0,v=0,o=0;
        set<int> s;
        // cout<<o/10<<endl;
        while(o!=n){
            ne = n;
            v=0;
            // cout<<"n:"<<n<<endl;
            while(ne>0){
                r = ne%10;
                ne = ne/10;
                v = v+r*r;
                // cout<<r<<" "<<ne<<" "<<v<<endl;
            }
            // cout<<v<<endl;
            o=n;
            n=v;
            if(n==1)
                return true;
            if(s.find(n)!=s.end())
                break;
            s.insert(n);
        }
        if(n==1)
            return true;
        return false;
    }
};