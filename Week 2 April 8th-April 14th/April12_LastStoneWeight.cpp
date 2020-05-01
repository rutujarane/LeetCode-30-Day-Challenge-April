class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        // make_heap(stones.begin(), stones.end());
        int a,b,c;
        // while(stones.size()>1){
        //     a = stones.front();
        //     pop_heap(stones.begin(), stones.end()); 
        //     stones.pop_back();
        //     b = stones.front();
        //     pop_heap(stones.begin(), stones.end()); 
        //     stones.pop_back();
        //     // cout << a << " " << b << endl;
        //     c = abs(a-b);
        //     if(c!=0){
        //         stones.push_back(c);
        //         push_heap(stones.begin(), stones.end());
        //     }
        // }
        priority_queue<int> q;
        for(int i=0; i<stones.size(); i++){
            q.push(stones[i]);
        }
        while(q.size()>1){
            a = q.top();
            q.pop();
            b = q.top();
            q.pop();
            c = abs(a-b);
            // cout << a << " " << b << endl;
            if(c!=0){
                q.push(c);
            }
        }
        if(q.size()>0)
            return q.top();
        return 0;
    }
};