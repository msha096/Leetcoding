class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # An ugly number must be multiplied by either 2, 3, or 5 from a smaller ugly number.
        l2 = 0
        l3 = 0
        l5 = 0
        num = [1]
        if n==1:
            return 1
        for i in range(n-1):
            nums = min(num[l2]*2, num[l3]*3, num[l5]*5) # multiple with the previous number, by remember the index
            if num[l2]*2 == nums:
                l2 += 1
            if num[l3]*3 == nums:
                l3 += 1
            if num[l5]*5 == nums:
                l5 += 1
            num.append(nums)
        #print(num)
        return nums