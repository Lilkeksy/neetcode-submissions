class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
        s_a = {}
        t_a = {}

        for i in s:
            if i in s_a:
                s_a[i] += 1
            else:
                s_a[i] = 1


        for i in t:
            if i in t_a:
                t_a[i] += 1
            else:
                t_a[i] = 1

        if s_a == t_a:
            return True
        else:
            return False