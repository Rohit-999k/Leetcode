class Solution(object):
    def getHint(self, secret, guess):
        sl = []
        gl = []

        A = 0
        for i in range(0,len(secret)):
            if secret[i]==guess[i]:
                A+=1
            else:
                sl.append(int(secret[i]))
                gl.append(int(guess[i]))

        B=0
        while(sl):
            if sl[0] in gl:
                B+=1
                gl.remove(sl[0])
            sl.pop(0)
        
        return str(A)+'A'+str(B)+'B'


        


        