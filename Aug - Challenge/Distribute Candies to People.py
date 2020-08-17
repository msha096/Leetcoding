class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        # this question can also be done in math way
        res = [0] * num_people
        r = 0
        while candies > 0:
            for i in range(num_people):
                dis = i+1 + r*num_people
                #print r, dis, i
                if candies <= dis:
                    res[i] += candies
                    return res
                res[i] += dis
                candies -= dis
            r += 1