class Solution {
    public boolean isPalindrome(int x) {
        if(x<0){
            return false;
        }
        int number =x;
        int reverseNum=0;
        int newNum=0;
        while(number!=0){
            newNum=number%10;
            reverseNum+=newNum;
            number=number/10;
            if(number!=0){
                reverseNum=reverseNum*10;
            }
        }
        if(reverseNum==x){
            return true;
        }
        else{
            return false;
        }
    }
}
