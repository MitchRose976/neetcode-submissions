class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sorted = list("".join(sorted(s)))
        t_sorted = list("".join(sorted(t)))
        return s_sorted == t_sorted