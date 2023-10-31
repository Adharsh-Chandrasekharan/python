A=[64,25,12,22,11]
for i in range(len(A)):
  for j in range(i+1,len(A)):
    if A[j]<A[i]:
      A[i],A[j]=A[j],A[i]

print(A)