class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        elem=set()
        for i in nums:
            if i in elem:
                return True
            elem.add(i)
        return False
