class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping charCount to list of Anagrams

        for s in strs:
            count = [0] * 26 # a ... z

            for c in s: # iterate through the char in each word
                count[ord(c) - ord("a")] += 1 #Find amount of times each character is used in the word
            
            res[tuple(count)].append(s) 
                        
            # Convert list to tuple because lists can’t be dictionary keys
            # (Tuples are immutable → safe to use as key)
            # Append the current word 's' to the list of its matching signature
            # If a new word has the exact same letters and same frequency of each letter then tuple(count) will match a key already in the dictionary

        return list(res.values())

        # Anagrams have the exact same letter counts
        # So basically we use a 26 length count array to represent each word's letters
        # Words with identical counts go to the same group 
        # Using a tuple lets us store the count as a dictionary key
