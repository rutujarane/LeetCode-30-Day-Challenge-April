class LRUCache {
    
    int cap;
    
    list< pair<int,int> > lru;     
    unordered_map< int, list<pair<int,int>>::iterator > h;   

    void moveFront(int key, int value) {
        
        lru.erase( h[key] ); 
        lru.push_front(make_pair(key, value));
        h[key] = lru.begin();
        
    }
    
public:
    LRUCache(int cap) {
        this->cap = cap;
    }
    
    int get(int key) {
        
        if(h.find(key) == h.end())
            return -1;
        int value = (*h[key]).second;
        moveFront(key, value);
        return (*h[key]).second;
        
    }
    
    void put(int key, int value) {
        
        if(h.find(key) != h.end()) {
            moveFront(key, value);
        }
        else {
            lru.push_front(make_pair(key, value));
            h[key] = lru.begin();
            if(h.size() > cap) {
                h.erase( lru.back().first );
                lru.pop_back();
            }
        }
        
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */