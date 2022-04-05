class Solution:
    def generate(self, n: int) -> List[List[int]]:
        ar=[]
        for i in range(1,n+1):
            x=[1]*i
            for j in range(1,i-1):
                x[j] = ar[-1][j-1] + ar[-1][j]    
            ar.append(x)
        return ar
    
                
