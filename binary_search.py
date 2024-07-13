from typing import List
class Solution:
    def search(self, nums : list[int], target : int ) -> int:
        l , r = 0 ,len(nums)-1
        while l <= r:
            m = (l+r) // 2
            if nums[m] > target:
                r = m-1
            elif nums[m] < target: 
                l = m+1
            else: return m
        return -1
  
    
nums = [-1, 0, 3, 5, 9, 12]
target = 9
s = Solution()
result = s.search(nums, target)

print(f"List: {nums}, Target: {target}, Result Index: {result}")
                
        
