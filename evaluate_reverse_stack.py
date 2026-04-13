def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in tokens:
            if i in ['+', '-', '*', '/']:
                top  = stack.pop()
                top1 = stack.pop()
                if i == '+':
                    count = top1 + top
                elif i == '-':
                    count = top1 - top
                elif i == '*':
                    count = top1 * top
                elif i == '/':
                    count = int(float(top1) / top)
                stack.append(count)
            else:
                stack.append(int(i))
        return stack[0]
