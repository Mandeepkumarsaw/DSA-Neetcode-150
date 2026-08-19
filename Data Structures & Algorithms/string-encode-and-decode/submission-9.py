class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # if all(len(e) == 0 for e in strs): 
        #     return str(len(strs)) 

        res = []
        for word in strs:
            encoded_str = str(len(word)) + "#" + word
            res.append(encoded_str)

        return "".join(res)    

                
        # if len(res)>0 and sum(len(s) for s in res):
        #     return " ".join(res) 
        # else:
        #     return "".join(res)     

    
    
    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        
        # if s.isdigit():
        #     return [""] * int(s) 
    
        # return s.split()
        
        res=[]
        i=0

        while i<len(s):
            j=i+1

            while s[j] != "#":
                j+=1

            length = int(s[i:j])

            word = s[j+1:j+1+length]
            res.append(word)

            i=j+1+length

        return res    

                

