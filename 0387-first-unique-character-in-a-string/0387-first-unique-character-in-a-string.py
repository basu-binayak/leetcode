class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_frequency = {}  # Dictionary to store character frequency

        # Count the frequency of each character
        for char in s:
            char_frequency[char] = char_frequency.get(char, 0) + 1

        # Find the first character with a frequency of 1
        for i, char in enumerate(s):
            if char_frequency[char] == 1:
                return i

        return -1  # If no non-repeating character is found
        
        
            