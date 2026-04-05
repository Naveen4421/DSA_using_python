def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stack1 = []
        stack2 = []
        
        for i in s:
            if i == '#':
                if stack1:        
                    stack1.pop()
            else:                
                stack1.append(i)
        
        for j in t:
            if j == '#':
                if stack2:       
                    stack2.pop()
            else:                
                stack2.append(j)
        
        return stack1 == stack2 
