class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped_str = re.sub(r'[^a-zA-Z0-9]', '', s.replace(" ", "").lower())
        if stripped_str == stripped_str[::-1]:
            return True
        else:
            return False