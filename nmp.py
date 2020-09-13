import sys


def display_menu():
	print("1. Add matrices")
	print("2. Multiply matrix to a constant")
	print("3. Multiply matrices")
	#print("4. Transpose matrix")
	#print("5. Calculate a determinant")
	#print("6. Inverse")
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


def scalar_multp(matrix1):
	scalar = int(input("Enter constant: "))
	matrix = [[matrix1[i][j] * scalar for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
	
	return matrix


def matrices_multp(matrix1, matrix2):
	matrix = [[sum(row * col for row, col in zip(X_row, Y_col)) for Y_col in zip(*matrix2)] for X_row in matrix1]
	
	return matrix


def main():
	while True:
		display_menu()
		user = input("Your choice: ")
		
		if user == '0':
			break
		
		r1, c1 = map(int, input("Enter size of first matrix: ").split())
		matrix_1 = create_matrix(r1)
		if user in ['1', '3']:
			r2, c2 = map(int, input("Enter size of second matrix: ").split())
			matrix_2 = create_matrix(r2)
				
		if user == '1':
			if r1 == r2 and c1 == c2:
				 result = addition(matrix_1, matrix_2)
				 print_matrix(result)
			else:
				 print('The operation cannot be performed')
		elif user == '2':
			result = scalar_multp(matrix_1)
			print_matrix(result)
		elif user == '3':
			if c1 == r2:
				result = matrices_multp(matrix_1, matrix_2)
				print_matrix(result)
			else:
				print('The operation cannot be performed')
		elif user == '4':
			result = transpose_matrix(matrix_1)
			print_matrix(result)
		elif user == '5':
			result = determinant(matrix_1)
			print_matrix(result)
		elif user == '6':
			result = inverse(matrix_1)
			print_matrix(result)
	
	
if __name__ == "__main__":
	main()
