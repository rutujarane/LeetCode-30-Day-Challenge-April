class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for st in strs:
            count = [0]*26
            for s in st:
                count[ord(s) - ord('a')] += 1
            ans[tuple(count)].append(st)
        print(ans)
        return ans.values()
        
        
            