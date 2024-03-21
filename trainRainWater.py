class Solution:
    def trap(self, height: List[int]) -> int:
        left_max=height[0]
        right_max=height[-1]
        left=0
        right=len(height)-1
        water_count=0
        water_count=0
        while(left<right):
            curr=left
            if(left_max>right_max):
                curr=right
            
            curr_count= min(left_max,right_max) - height[curr]
            if(curr_count>0):
                water_count+=curr_count

            if(left_max<height[left]):
                left_max=height[left]

            if(right_max < height[right]):
                right_max= height[right]
                
            if left_max <= right_max :
                left+=1
            else:
                right-=1
                
        return water_count
