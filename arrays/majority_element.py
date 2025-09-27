# majority_element.py
# Problem: Majority Element (LeetCode)
# Approach: Moore Voting algorithm — tracks candidate with count balance

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
   
        count,candidate=0,None
        for i in nums:
            if count==0:
                candidate=i
                count=1
            elif i==candidate:
                count+=1
            else:
                count-=1
        return candidate
