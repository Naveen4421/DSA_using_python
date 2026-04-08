def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        alt=0
        max_alt=0
        for i in gain:
            alt+=i
            max_alt=max(max_alt,alt)
        return max_alt
