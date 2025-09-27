# rotate_array.py
# Problem: Rotate Array (LeetCode)
# Approach: Slice-based rotation using temporary buffer and in-place overwrite

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        temp=[]
        temp.extend(nums[len(nums)-k:])
        temp.extend(nums[:len(nums)-k])
        for i,val in enumerate(temp):
            nums[i]=val
