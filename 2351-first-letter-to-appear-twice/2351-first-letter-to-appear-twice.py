class Solution:
    def repeatedCharacter(self, s: str) -> str:
        # Here's the logic to solve the problem:

        # Initialize an empty dictionary letter_indices to store the indices where
        # each letter appears.
        char_dict={}
        
        # Iterate through the characters in the string s from left to right.
        for i,char in enumerate(s):
            # For each character, check if it already exists in the letter_indices
            # dictionary.
            if char not in char_dict.keys():
                # If it does not exist, add the letter to the dictionary with its
                # current index.
                char_dict[char]=i
            # If it exists, it means the letter has appeared before. Check the
            # index from the dictionary and return the letter.
            else:
                return char