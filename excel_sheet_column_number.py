def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        result=0
        for c in columnTitle:
            value=ord(c)-ord("A")+1
            result=result*26+value
        return result
