class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        lookup = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        
        def vowels(s):
            n=0
            for c in s:
                if c in lookup:n+=1
            return n
        mid = len(s)//2
        return vowels(s[:mid])==vowels(s[mid:])    
        
    
     
    
    
    
                
        
        
         
            
          
            
        