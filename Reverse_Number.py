class Solution:
    def reverse(self, x: int) -> int:
        if(x> ((2**(31)) -1) or x< -1*2**(31)):
            return 0
        old_num=abs(x)
        new_num=0
        counter=0
        scale=1
        
        while old_num>0:
            print(old_num)
            new_num= new_num * scale + old_num%10
            print(new_num)
            old_num=old_num//10
            scale=10
        if(x<0):
            new_num=new_num*-1

        if(new_num> ((2**(31)) -1) or new_num< -1*2**(31)):
            return 0

        return new_num
