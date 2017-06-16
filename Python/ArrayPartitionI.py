class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        sorted_nums=sorted(nums)
        return sum(sorted_nums[0::2])
