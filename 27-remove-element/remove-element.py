class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0  # Slow pointer for next non-val position
        for j in range(len(nums)):  # Fast pointer scans all elements
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i