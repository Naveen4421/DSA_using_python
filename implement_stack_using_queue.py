class MyStack(object):

    def __init__(self):
        self.queue=[]

        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue.append(x)
        
        

    def pop(self):
        """
        :rtype: int
        """
        return self.queue.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.queue[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        if(len(self.queue)==0):
            return True
        else:
            return False
