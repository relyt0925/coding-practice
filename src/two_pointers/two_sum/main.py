class Solution:
    def twoSum(self, nums: List[int], target: int) -> bool:
        if len(nums) == 0:
            return False
        left, right = 0, len(nums) - 1
        while left != right:
            current_sum = nums[left] + nums[right]
            if current_sum == target:
                return True
            if current_sum > target:
                right = right - 1
            if current_sum < target:
                left = left + 1
        return False