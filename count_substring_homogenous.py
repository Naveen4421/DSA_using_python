class Solution(object):
    def countHomogenous(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD=10**9+7
        total=0
        run_length=1
        
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                run_length+=1
            else:
                total+=run_length*(run_length+1)//2
                run_length=1

        total+=run_length*(run_length+1)//2

        return total%MOD


        
