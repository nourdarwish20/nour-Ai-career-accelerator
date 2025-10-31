def find_triplets(L):
   M=set()
   T=sorted(L)
   print(T)
   for i in range(len(T)):#take first nb indices
        for j in range(i + 1, len(T)):#second and ensure hat not same as the first 
          for k in range(j + 1, len(T)):#third
             if T[i]+T[j]+T[k]==0:
                    M.add((T[i],T[j],T[k]))
                        
   return [list(t) for t in M]  # convert back to list
L=[-1,0,1,2,-1,-4]   
res=find_triplets(L)
print(res)     