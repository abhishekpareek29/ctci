def zero_mat(mat):
  row = set()
  col = set()

  for i in range(len(mat)):
    for j in range(len(mat[0])):
      if mat[i][j] == 0:
        row.add(i)
        col.add(j)
  for x in row:
    for i in range(len(mat[0])):
      mat[x][i] = 0
  for x in col:
    for i in range(len(mat)):
      mat[i][x] = 0

  return mat

if __name__ == "__main__":
  mat = [[0,2,3,4],
         [1,12,3,4],
         [1,2,0,4],
         [1,2,3,4]]
  zero_matrix = zero_mat(mat)
  print(zero_matrix[0])
  print(zero_matrix[1])
  print(zero_matrix[2])
  print(zero_matrix[3])
