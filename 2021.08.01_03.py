row, col = map(int, input().split())
matrix = []
result = 0
for i in range(row):
  tmp = list(map(int, input().split()))
  tmp.sort()
  matrix.append(tmp)
for i in range(row):
  if matrix[result][0] <= matrix[i][0]:
    result = i
print(matrix[result][0])


