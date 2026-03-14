def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        mapping={')':'(','}':'{',']':'['}
        for char in s:
            if char in '({[':
                stack.append(char)
            elif char in ')}]':
                if not stack:
                    return False
                top=stack.pop()
                if mapping[char]!=top:
                    return False
        return len(stack)==0
