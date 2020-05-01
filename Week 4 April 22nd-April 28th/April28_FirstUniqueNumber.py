class FirstUnique:

    
    def __init__(self, nums: List[int]):
        
        self.cach = Counter(nums)
        self.unique = deque(nums)
        
        # self.unique = set()
        # self.everything = []
        # heapq.heapify(self.everything)
        # for i in nums:
        #     self.add(i)

    def showFirstUnique(self) -> int:
        
        while self.unique and self.cach[self.unique[0]] != 1: 
            self.unique.popleft()
        if self.unique:
            return self.unique[0]
        else:
            return -1
        
        # if not self.unique:
        #     return -1
        # return next(iter(self.unique))

    def add(self, value: int) -> None:
        self.cach[value] += 1
        self.unique.append(value)
        
        # if value not in self.everything:
        #     heapq.heappush(self.everything,value)
        #     self.unique.add(value)
        # else:
        #     if value in self.unique:
        #         self.unique.remove(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)