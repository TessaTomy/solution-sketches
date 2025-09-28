# candy_distribution.py
# Problem: Candy (LeetCode)
# Approach: Two-pass greedy — left-to-right and right-to-left rating comparison

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        candy = [1] * n  
        
        # Step 2: Left to right
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candy[i] = candy[i - 1] + 1

        # Step 3: Right to left
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candy[i] = max(candy[i], candy[i + 1] + 1)

        return sum(candy)
