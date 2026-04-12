def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        c=""
        for ch in s:
            if ch.isalnum():
                c+=ch.lower()
        return c==c[::-1]
