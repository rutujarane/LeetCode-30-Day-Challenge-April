class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        summ = 0
        a = dict()
        a[0] = 1
        for i in range(len(nums)):
            summ += nums[i]
            if (summ - k) in a:
                count += a.get(summ - k)
            a[summ] = a.get(summ, 0) + 1
        return count