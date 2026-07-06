class Solution(object):
    def countConsistentStrings(self, allowed, words):
        allowed_set = set(allowed)
        count = 0
        for word in words:
            for ch in word:
                if not ch in  allowed_set:
                    break
            else:
                count+=1    
                       
           
    

       

                       
            
        return count         



               


                









        
        