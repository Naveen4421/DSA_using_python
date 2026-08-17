class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        result=[]
        stack=[]
        for i in s:
            if i =="(":
                if stack:
                    result.append(i)
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    result.append(i)
        return ''.join(result)


        
