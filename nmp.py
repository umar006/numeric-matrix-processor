def display_menu():
   print("1. Add matrices")
   print("2. Multiply matrix to a constant")
   print("3. Multiply matrices")
   print("4. Transpose matrix")
   print("5. Calculate a determinant")
   print("6. Inverse")
   print("0. Exit")
   
   
def create_matrix(rows):
   mat = []
   for i in range(rows):
      row = map(float, input().split())
      mat.append([r for r in row])
   
   return mat
   

def print_matrix(matrix):
   print("The result is")
   for row in matrix:
      for col in row:
         print(col, end=' ')
      print('')
   print('')
        

def addition(matrix1, matrix2):
   matrix = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
   
   return matrix


def scalar_multiplication(matrix1):
   scalar = int(input("Enter constant: "))
   matrix = [[matrix1[i][j] * scalar for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
   
   return matrix


def multiplication(matrix1, matrix2):
   matrix = [[sum(row * col for row, col in zip(X_row, Y_col)) for Y_col in zip(*matrix2)] for X_row in matrix1]
   
   return matrix
   
   
def transpose(matrix1, c):
   if c == '1':
      matrix = [list(t) for t in zip(*matrix1)]
   elif c == '2':
      matrix = [list(t)[::-1] for t in zip(*matrix1)][::-1]
   elif c == '3':
      matrix = [t[::-1] for t in matrix1]
   elif c == '4':
      matrix = matrix1[::-1]
   
   return matrix


def determinant(matrix1, total=0):
   # Section 1: store indices in list for row referencing
   indices = list(range(len(matrix1)))
   
   # Section 2: when at 1x1 submatrices recursive call end
   if len(matrix1) == 1:
      return matrix1[0][0]
   # Section 3: when at 2x2 submatrices recursive calls end
   if len(matrix1) == 2 and len(matrix1[0]) == 2:
     val = matrix1[0][0] * matrix1[1][1] - matrix1[1][0] * matrix1[0][1]
     return val
   
   # Section 3: define submatrix for focus column and 
   #      call this function
   for fc in indices: # A) for each focus column, ...
     # find the submatrix ...
     As = [row[:] for row in matrix1] # B) make a copy, and ...
     As = As[1:] # ... C) remove the first row
     height = len(As) # D) 
   
     for i in range(height): 
         # E) for each remaining row of submatrix ...
         #     remove the focus column elements
         As[i] = As[i][0:fc] + As[i][fc+1:] 
   
     sign = (-1) ** (fc % 2) # F) 
     # G) pass submatrix recursively
     sub_det = determinant(As)
     # H) total all returns from recursion
     total += sign * matrix1[0][fc] * sub_det 
   
   return total
   
   
def inverse(matrix1, total=0):   
   # Section 1: Make copies of A & I, AM & IM, to use for row ops
   n = len(matrix1)
   AM = [row[:] for row in matrix1]
   I = []
   for i in range(n):
      row = []
      for j in range(n):
         if i == j:
            row.append(1)
         else:
            row.append(0)
      I.append(row)
   IM = [row[:] for row in I]
   
   # Section 2: Perform row operations
   indices = list(range(n)) # to allow flexible row referencing ***
   for fd in range(n): # fd stands for focus diagonal
      fdScaler = 1.0 / AM[fd][fd]
      # FIRST: scale fd row with fd inverse. 
      for j in range(n): # Use j to indicate column looping.
         AM[fd][j] *= fdScaler
         IM[fd][j] *= fdScaler
      # SECOND: operate on all rows except fd row as follows:
      for i in indices[0:fd] + indices[fd+1:]: 
         # *** skip row with fd in it.
         crScaler = AM[i][fd] # cr stands for "current row".
         for j in range(n): 
             # cr - crScaler * fdRow, but one element at a time.
             AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
             IM[i][j] = IM[i][j] - crScaler * IM[fd][j]
   return IM
   

def main():
   while True:
      display_menu()
      user = input("Your choice: ")
      
            
      if user == '1':
         r1, c1 = map(int, input("Enter size of first matrix: ").split())
         matrix_1 = create_matrix(r1)
         r2, c2 = map(int, input("Enter size of second matrix: ").split())
         matrix_2 = create_matrix(r2)
         
         if r1 == r2 and c1 == c2:
             result = addition(matrix_1, matrix_2)
             print_matrix(result)
         else:
             print('The operation cannot be performed')
      elif user == '2':
         r1, c1 = map(int, input("Enter size of first matrix: ").split())
         matrix_1 = create_matrix(r1)
      
         result = scalar_multiplication(matrix_1)
         print_matrix(result)
      elif user == '3':
         r1, c1 = map(int, input("Enter size of first matrix: ").split())
         matrix_1 = create_matrix(r1)
         r2, c2 = map(int, input("Enter size of second matrix: ").split())
         matrix_2 = create_matrix(r2)
         
         if c1 == r2:
            result = multiplication(matrix_1, matrix_2)
            print_matrix(result)
         else:
            print('The operation cannot be performed')
      elif user == '4':
         print('\n1. Main diagonal')
         print('2. Side diagonal')
         print('3. Vertical diagonal')
         print('4. Horizontal diagonal')
         choice = input("Your choice: ")
         r1, c1 = map(int, input("Enter size of first matrix: ").split())
         matrix_1 = create_matrix(r1)
         
         result = transpose(matrix_1, choice)
         print_matrix(result)
      elif user == '5':
         r1, c1 = map(int, input("Enter size of first matrix: ").split())
         matrix_1 = create_matrix(r1)
         
         result = determinant(matrix_1)
         print("The result is:\n", result)
      elif user == '6':
         r1, c1 = map(int, input("Enter size of first matrix: ").split())
         matrix_1 = create_matrix(r1)
         
         if len(matrix_1) == len(matrix_1[0]) and determinant(matrix_1) != 0:
            result = inverse(matrix_1)
            print_matrix(result)
         else:
            print("This matrix doesn't have an inverse")
      elif user == '0':
         break
   
   
if __name__ == "__main__":
   main()
