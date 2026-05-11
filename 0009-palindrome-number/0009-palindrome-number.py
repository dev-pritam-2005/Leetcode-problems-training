class Solution(object):
    def isPalindrome(self, x):
       
        original_x = x
        sum = 0
        
        if x < 0:
            return False

      
        temp = x
        while temp > 0:
            rem = temp % 10
            sum = sum * 10 + rem
            temp = temp // 10
            
        return original_x == sum


