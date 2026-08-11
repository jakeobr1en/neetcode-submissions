class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        d = dict()

        for s in strs:
            key = "".join(sorted(s))
            d.setdefault(key, []).append(s)

        for k in d:
            output.append(d[k])

        return output