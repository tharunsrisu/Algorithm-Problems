class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_length=len(t)
        s_length=len(s)
        
        if(s_length!=t_length):
            return False

        count_dic={}
        for i in range(0,s_length):
            if s[i] not in count_dic:
                count_dic[s[i]]=1
            else:
                count_dic[s[i]]+=1

        for j in range(0,t_length):
            if( t[j] not in count_dic):
                return False
            count_dic[t[j]]-=1

        for items in count_dic:
            if count_dic[items]<0 or count_dic[items]> 0:
                return False

        return True
