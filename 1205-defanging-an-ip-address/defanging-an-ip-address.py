class Solution(object):
    def defangIPaddr(self, address):
        address=list(address)
        lst=[]
        for i in range(len(address)):
            if address[i]==".":
                lst.append("[.]")
            else:
                lst.append(address[i])
        return "".join(lst)            
