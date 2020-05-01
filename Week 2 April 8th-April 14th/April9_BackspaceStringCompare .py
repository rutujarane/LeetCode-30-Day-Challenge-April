class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s1 = ''
        s2 = ""
        for i in range(len(S)):
            if(S[i]=='#'):
                s1 = s1[:-1]
            else:
                s1 += S[i]
        # print(s1);
        for i in range(len(T)):
            if(T[i]=='#'):
                s2 = s2[:-1]
                # print(s2)
            else:
                s2 += T[i]
        # print(s2);
        if s1==s2:
            return True
        return False