def __init__(self):
        self.stack=[]
        self.minstack=[]
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if len(self.minstack)==0 or val<=self.minstack[-1]:
            self.minstack.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        if(len(self.stack)==0):
            return "the stack is empty"
        else:
            top=self.stack.pop()

        if top==self.minstack[-1]:
            return self.minstack.pop()
        else:
            return "top element is not matched"
        

    def top(self):
        """
        :rtype: int
        """
        if(len(self.stack)==0):
            return "the stack is empty"
        else:
            return self.stack[-1]
        
        

    def getMin(self):
        """
        :rtype: int
        """
        if(len(self.minstack)==0):
            return "min stack is empty"
        else:
            return self.minstack[-1]
