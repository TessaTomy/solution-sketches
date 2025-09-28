# product_except_self.py
# Problem: Product of Array Except Self (LeetCode)
# Approach: Total product with division, zero-count logic for edge cases

class Solution(object):
    def productExceptSelf(self,nums):
        total_product = 1
        zero_count = 0

        # Step 1: Compute product of non-zero elements
        for num in nums:
            if num != 0:
                total_product *= num
            else:
                zero_count += 1

        # Step 2: Build output based on zero count
        result = []
        for num in nums:
            if zero_count > 1:
                result.append(0)  # More than one zero → everything is zero
            elif zero_count == 1:
                result.append(total_product if num == 0 else 0)
            else:
                result.append(total_product // num)

        return result
