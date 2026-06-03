def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        ans = float('inf')

        # Order 1: Best land first, then each water
        min_land_end = min(s + d for s, d in zip(landStartTime, landDuration))
        for ws, wd in zip(waterStartTime, waterDuration):
            ans = min(ans, max(min_land_end, ws) + wd)

        # Order 2: Best water first, then each land
        min_water_end = min(s + d for s, d in zip(waterStartTime, waterDuration))
        for ls, ld in zip(landStartTime, landDuration):
            ans = min(ans, max(min_water_end, ls) + ld)

        return ans
