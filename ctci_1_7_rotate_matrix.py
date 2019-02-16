def rotate_matrix(image):
  n = len(image) - 1
  for i in range(int(len(image)/2)):
    temp = None
    for j in range(i, int(len(image)/2)):
      temp = image[j][n]
      image[j][n-i] = image[n-i][n-j]
      image[n-i][n-j] = image[n-j][i]
      image[n-j][i] = image[i][j]
      image[i][j] = temp
      print(image[0])
      print(image[1])
      print(image[2])
      print(image[3])
      print("========")
  return image

if __name__ == "__main__":
  image = [[1,2,3,4],
           [1,2,3,4],
           [1,2,3,4],
           [1,2,3,4]]
  rotated_matrix = rotate_matrix(image)
  print(rotated_matrix[0])
  print(rotated_matrix[1])
  print(rotated_matrix[2])
  print(rotated_matrix[3])
