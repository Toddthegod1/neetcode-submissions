class Solution:
    # ENCODE: Convert list of strings into a single encoded string
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # Format: length_of_string + "#" + string
            # Example: "lint" -> "4#lint"
            res += str(len(s)) + "#" + s
        return res
     # DECODE: Convert encoded string back into the original list of strings
    def decode(self, s: str) -> List[str]:
        res, i = [], 0  # res holds decoded strings, i is current index in s

        while i < len(s):  # Continue until we reach the end of the encoded string
            j = i
            # Move j forward until we find the "#"
            # Characters between i and j form the length of the next word
            while s[j] != "#":
                j += 1
            # Extract the number (length of the string)
            # Convert substring chars into an integer
            length = int(s[i:j])
            # Extract the actual string:
            # It starts at j+1 and spans 'length' characters
            res.append(s[j + 1 : j + 1 + length])
            # Move i to the start of the next encoded chunk
            i = j + 1 + length
        return res

