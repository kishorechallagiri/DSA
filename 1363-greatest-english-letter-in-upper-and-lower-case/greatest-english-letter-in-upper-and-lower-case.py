class Solution(object):
    def greatestLetter(self, s):
        m=""
       
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if s[i].lower()==s[j].lower() and s[i]!=s[j]:
                    if s[i].upper()>m:
                        m=s[i].upper()
              
        return m        
        