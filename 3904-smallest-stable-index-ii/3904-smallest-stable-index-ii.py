class Solution(object):
    def firstStableIndex(self, nums, k):
        n = len(nums)
        if n == 0:
            return -1

        suff_min = [0] * n
        curr_min = nums[-1]
        for i in range(n - 1, -1, -1):
            curr_min = min(curr_min, nums[i])
            suff_min[i] = curr_min

        running_max = nums[0]
        for i in range(n):
            running_max = max(running_max, nums[i])

            if running_max - suff_min[i] <= k:
                return i

        return -1
        