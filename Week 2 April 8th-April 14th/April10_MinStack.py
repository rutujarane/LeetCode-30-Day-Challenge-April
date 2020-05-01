class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []
        self.min = float('inf')

    def push(self, x: int) -> None:
        m = []
        m.append(x)
        if x<self.min:
            self.min = x
        m.extend(self.l)
        self.l = m
        # print(self.l)

    def pop(self) -> None:
        if self.l[0]==self.min:
            self.min = float('inf')
        self.l = self.l[1:]
        # print(self.l)

    def top(self) -> int:
        if self.l:
            print(self.l[0])
            return self.l[0]
        return

    def getMin(self) -> int:
        # if self.min<float('inf'):
        #     print('min=',self.min)
        #     return self.min
        minv = float('inf')
        for i in self.l:
            if minv > i:
                minv = i
        # print('minv=',minv)
        return minv


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()