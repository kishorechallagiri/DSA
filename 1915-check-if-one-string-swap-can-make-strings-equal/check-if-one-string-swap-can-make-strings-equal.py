class Solution(object):
    def areAlmostEqual(self, s1, s2):
        if s1==s2:
            return True
        s2=list(s2)
        for i in range(len(s2)):
            for j in range(i+1,len(s2)):
                s2[i],s2[j]=s2[j],s2[i]
                if "".join(s2)==s1:
                    return True
                s2[i],s2[j]=s2[j],s2[i] 
        
        return False