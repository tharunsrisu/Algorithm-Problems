class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count={} # Hashmap of character counts
        for i in s:
            if i not in char_count:
                char_count[i]=1
            else:
                char_count[i]+=1
        
        ind=0
        for i in s:
            if char_count[i]==1:
                return ind
            ind+=1
        
        return -1
