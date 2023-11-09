def spiral(matrix):
  c=1
  for j in range(len(matrix)):
    if c%2!=0:
      for i in range(len(matrix[j])):
        print(matrix[j][i],end=" ")
    else:
      for i in range(len(matrix[j])-1,-1,-1):
        print(matrix[j][i],end=" ")
    c+=1
  




matrix=[[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]]

spiral(matrix)