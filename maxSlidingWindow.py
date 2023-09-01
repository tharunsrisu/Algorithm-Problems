class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        arr1=[]
        max1=0
        index1=0
        length1=len(nums)
        for i in range(0,k):
            if(nums[i]>=max1):
                max1=nums[i]
                index1=i
        arr1.append(max1)
        start=1
        for j in range(k,length1):
            if(start<=index1 and j>=index1):
                if(max1<=nums[j]):
                    max1=nums[j]
                    index1=j
            else:
                max1=nums[j]
                index1=j
                for l in range(start, j+1):
                    if(max1<=nums[l]):
                        max1=nums[l]
                        index1=l
            
            arr1.append(max1)
            start+=1
            
        return arr1