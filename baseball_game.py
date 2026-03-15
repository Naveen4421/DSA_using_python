def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack=[]
        sum_=0
        for i in operations:
            if i=='D':
                top=stack[-1]
                top=top*2
                stack.append(top)

            elif i=='C':
                stack.pop()
            elif i=='+':
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(i))
        return sum(stack)
