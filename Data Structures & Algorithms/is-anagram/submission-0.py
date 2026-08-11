class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = {}
        t_count = {}
        for n in s:
            if s_count.get(n):
                s_count[n] += 1
            else: 
                s_count[n] = 1
        
        for n in t:
            if t_count.get(n):
                t_count[n] += 1
            else: 
                t_count[n] = 1
        
        if s_count == t_count:
            return True
        return False