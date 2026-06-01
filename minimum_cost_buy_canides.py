def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost)<=2:
            return sum(cost)
        min_cost=0
        cost=sorted(cost,reverse=True)
        for i in range(len(cost)):
            if (i+1)%3==0:
                continue
            else:
                min_cost+=cost[i]
        return min_cost
