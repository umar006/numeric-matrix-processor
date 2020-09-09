def create_matrix(rows):
   mat = []
   for i in range(rows):
      row = map(int, input().split())
      mat.append([r for r in row])

   return mat
   

def addition(matrix1, matrix2):
   matrix = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

   return matrix


def print_matrix(matrix):
    for row in matrix:
        for col in row:
            print(col, end=' ')
        print('')
    
    
r1, c1 = map(int, input().split())
matrix_1 = create_matrix(r1)

r2, c2 = map(int, input().split())
matrix_2 = create_matrix(r2)

if r1 == r1 and c1 == c2:
    result = addition(matrix_1, matrix_2)
    print_matrix(result)
else:
    print('ERROR')
