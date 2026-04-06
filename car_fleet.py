def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        cars = sorted(zip(position, speed), reverse=True)
    
        fleets = 0
        prev_time = -1
        
        for pos, spd in cars:
            time = float(target - pos) / spd   
            
            if time > prev_time:          # IMPORTANT: only >
                fleets += 1
                prev_time = time
        
        return fleets
