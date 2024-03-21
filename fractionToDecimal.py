class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        negative= False
        if(numerator < 0 and denominator < 0):
            numerator= numerator*(-1)
            denominator = denominator *(-1)
            
        elif (numerator <0):
            numerator= numerator*(-1)
            negative=True

        elif (denominator < 0):
            denominator = denominator *(-1)
            negative=True

        decim=numerator//denominator
        rem=numerator % denominator
        if(rem ==0):
            return str(decim)

        result= str(decim)
        rem_dic={}
        result+="."
        while rem!=0 and rem not in rem_dic:
            rem_dic[rem]= len(result)
            rem *=10
            result+= str(rem//denominator)
            rem %= denominator

        if rem in rem_dic:
            result= result[:rem_dic[rem]] + "(" + result[rem_dic[rem]:]+")"
        
        return result
