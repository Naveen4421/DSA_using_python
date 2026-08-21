class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        n = len(s)
        
        # Step 1: skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1
        
        # Step 2: check for sign (only ONE, right after whitespace)
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1
        
        # Step 3: collect digits until a non-digit is found
        digits = []
        while i < n and s[i].isdigit():
            digits.append(s[i])
            i += 1
        
        # Step 4: if no digits were collected, return 0
        if not digits:
            return 0
        
        # Step 5: convert collected digits to a number, apply sign
        result = int(''.join(digits)) * sign
        
        # Step 6: clamp to 32-bit signed integer range
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        
        return result

        
