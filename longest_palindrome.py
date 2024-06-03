class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        The algorithm can be split into two parts.
        1) Iterating through the stirng
        2) check at each position if you can make a palindrome.

        We are not going for all possible substrings.
           - You can do this with a array keeping track of substrings
           - Iterate through string and for each new string, we add it to array of subtring and
             and add the character to beginning of string of each exisiting substring
        we are infact going for all possible palindromes only
        '''
        length_s=len(s)
        def max_palindromes (l,r):
            counter=0
            curr_string=""
            while l >-1 and r < length_s and s[l]==s[r]:
                counter+=1
                curr_string=s[l:r+1]
                l-=1
                r+=1

            return curr_string


        max_length=0
        curr_max_string=""
        for i in range(0,length_s):
            s1=max_palindromes(i, i)
            s2=max_palindromes(i, i+1) 

            if(len(s1) >=len(s2) and len(s1)>=max_length):
                max_length=len(s1)
                curr_max_string=s1
            elif(len(s2)>=len(s1) and len(s2)>=max_length):
                max_length=len(s2)
                curr_max_string=s2
                
        return curr_max_string
        
        return max_length
