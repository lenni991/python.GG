class Solution:
    def two_sum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j

reuslt = Solution().two_sum([2, 7, 11, 15], 9)
print(reuslt)
