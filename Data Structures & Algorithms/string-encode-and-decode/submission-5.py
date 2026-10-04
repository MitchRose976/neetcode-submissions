class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for value in strs:
            encoded += str(len(value)) + '#' + value

        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        index = 0
        while index != len(s):
            adjusted_str = s[index:]

            # Trim off delimiter - ex: "5#", "11#"
            delimiter_len = adjusted_str.find('#') + 1
            # Get length of string excluding delimiter
            str_len = int(adjusted_str.split('#')[0])

            decoded_str = adjusted_str[delimiter_len:str_len + delimiter_len]
            decoded.append(decoded_str)

            # Adjust index to exclude portion just parsed in next loop
            index = index + (str_len + delimiter_len)
        
        return decoded