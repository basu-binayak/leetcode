class Solution:
    def reverse(self, x: int) -> int:
        # Define the 32-bit signed integer range boundaries
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        # Step 1: Extract the sign
        sign = 1 if x >= 0 else -1

        # Step 2: Convert absolute value to string and reverse it
        reversed_str = str(abs(x))[::-1]

        # Step 4: Convert the reversed string back to an integer
        reversed_num = int(reversed_str)

        # Step 5: Apply the sign
        reversed_num *= sign

        # Step 6: Check if the reversed integer is within the 32-bit signed integer range
        if reversed_num < INT_MIN or reversed_num > INT_MAX:
            return 0

        return reversed_num


