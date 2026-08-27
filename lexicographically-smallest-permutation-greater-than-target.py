class Solution(object):
    def lexGreaterPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """
        n = len(s)
        count = [0] * 26
        for ch in s:
            count[ord(ch) - 97] += 1

        cur = count[:]
        best_i = -1
        best_snapshot = None

        for i in range(n):
            t = ord(target[i]) - 97

            
            if any(cur[c] > 0 for c in range(t + 1, 26)):
                best_i = i
                best_snapshot = cur[:]

            
            if cur[t] > 0:
                cur[t] -= 1
            else:
                break  

        if best_i == -1:
            return ""

        result = list(target[:best_i])
        cur = best_snapshot
        t = ord(target[best_i]) - 97

        
        for c in range(t + 1, 26):
            if cur[c] > 0:
                cur[c] -= 1
                result.append(chr(c + 97))
                break

        
        for c in range(26):
            result.extend([chr(c + 97)] * cur[c])

        return ''.join(result)
        
