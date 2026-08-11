class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped = "".join(c for c in s.lower() if c.isalnum())
        print(stripped)
        i = 0
        j = len(stripped)

        while i < j:
            if stripped[i] == stripped[j-1]:
                i = i+1
                j = j-1
            else:
                return False
            
        return True