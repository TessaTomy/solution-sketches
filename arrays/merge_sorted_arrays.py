# merge_sorted_arrays.py
# Problem: Merge Sorted Array (LeetCode)
# Approach: Two-pointer merge with temporary buffer, then in-place overwrite

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None. Do not return anything, modify nums1 in-place instead.
        """
        if not nums1:
            nums1[:] = nums2
        elif not nums2:
            pass
        else:
            i, j = 0, 0
            temp = []

            
            while i < m and j < n:
                if nums1[i] < nums2[j]:
                    temp.append(nums1[i])
                    i += 1
                else:
                    temp.append(nums2[j])
                    j += 1

            # Append remaining elements
            temp.extend(nums1[i:m])
            temp.extend(nums2[j:n])

            # In-place 
            for k in range(m + n):
                nums1[k] = temp[k]
