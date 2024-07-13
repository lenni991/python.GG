class Solution(object):
    def threeConsecutiveOdds(self, arr):
        for i in range(len(arr) - 2):
            if arr[i] % 2 == 1 and arr[i + 1] % 2 == 1 and arr[i + 2] % 2 == 1:
                return True
        return False



# Example usage:
s = Solution()
arr1 = [2, 6, 4,5,3,11, 1, 8, 3, 2, 7]
print(s.threeConsecutiveOdds(arr1))

