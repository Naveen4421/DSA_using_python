class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        total = 0

        for num in range(num1, num2 + 1):
            digits = str(num)

            for i in range(1, len(digits) - 1):
                if ((digits[i] > digits[i - 1] and digits[i] > digits[i + 1]) or
                    (digits[i] < digits[i - 1] and digits[i] < digits[i + 1])):
                    total += 1

        return total
