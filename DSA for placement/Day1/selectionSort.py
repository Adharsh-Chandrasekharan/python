A=[64,25,12,22,11]
for i in range(len(A)):
  minid=i
  for j in range(i+1,len(A)):
    if A[minid] > A[j]:
      minid = j
    A[i],A[minid] = A[minid] , A[i]

print("Sorted..")
print(A)