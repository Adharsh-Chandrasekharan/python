def setMatrixZero(matrix):
  zeros=[]
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      if matrix[i][j]==0:
        zeros.append([i,j])
  for i in range(len(zeros)):
    for j in range(len(matrix)):
      matrix[j][zeros[i][1]]=0
      matrix[zeros[i][0]][j]=0

  return matrix


matrix=[[1,1,1],
        [1,0,1],
        [1,1,1]]

zeros=setMatrixZero(matrix)
print(zeros)