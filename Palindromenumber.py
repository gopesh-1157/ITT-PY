class Solution(object):
    def isPalindrome(self, x):
        # Convert the integer to a string
        b = str(x)
        
        # Check if the string is equal to its reverse
        # b[::-1] reverses the string
        if b[::-1] == b:
            return True   # It is a palindrome
        else:
            return False  # Not a palindrome
