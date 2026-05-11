class Solution(object):
    def isPalindrome(self, x):
      
        n = x 
        
   
        if n < 0:
            return False 

        b = n
        reverse = 0 
        
     
        while n > 0:
            rem = n % 10
            reverse = reverse * 10 + rem
            n = n // 10
            

        return b == reverse


