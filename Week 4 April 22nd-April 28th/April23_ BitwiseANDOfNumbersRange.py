class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        #5: 101
        #6: 110
        #7: 111
        #a: 100
        mb = self.binary(m)
        nb = self.binary(n)
        i = 0
        s = ""
        if len(mb) < len(nb):
            mb = mb[::-1]
            while len(mb) < len(nb):
                mb.append(0)
            mb = mb[::-1]
        elif len(nb) < len(mb):
            nb = nb[::-1]
            while len(nb) < len(mb):
                nb.append(0)
            nb = nb[::-1]
        while mb[i]==nb[i]:
            if mb[i]==1:
                s += '1'
            else:
                s += '0'
            i += 1
            if i==len(mb):
                break
                
        while i<len(mb):
            s += '0'
            i += 1
        sd = self.decimal(s)
        return sd
        
    def binary(self, m: int):
        s = []
        if m==0:
            s.append(0)
            return s
        while m>0:
            r = m%2
            s.append(r)
            m = math.floor(m/2)
        s = s[::-1]
        return s
            
    def decimal(self, s: str):
        sd = 0
        s = s[::-1]
        for i in range(len(s)):
            sd += int(s[i])*int(math.pow(2,i))
        return sd