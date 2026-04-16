class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in strs:
            sortk = ''.join(sorted(i))
            res [sortk].append(i)
        return list(res.values())



        

