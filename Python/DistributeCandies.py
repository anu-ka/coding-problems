class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        if len(candies) == 0 or len(candies)%2 !=0:
            return 0
        h = set()
        for i in candies:
            h.add(i)
        l=len(candies)/2
        if(len(h)>l):
            return int(l)
        return len(h)
