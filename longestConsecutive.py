class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elements= set()
        for i in nums:
            if i not in elements:
                elements.add(i)
        curr_max=0
        for elem in elements:
            if(elem-1 not in elements):
                curr_elem=elem
                curr_count=0
                while curr_elem in elements:
                    curr_count+=1
                    curr_elem+=1
                curr_max=max(curr_max,curr_count)
                
        return curr_max
