class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        for el in range(len(self.matrix)):
            for num in range(len(self.matrix[el])):
                self.matrix[el][num] += other.matrix[el][num]
        return Matrix(self.matrix)

    def __str__(self):
        for el in range(len(self.matrix)):
            for num in range(len(self.matrix[el])):
                print(f'{self.matrix[el][num]:<4}    ', end='')
            print()
        return ''


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_2 = Matrix([[7, 8], [9, 10], [7, 8]])
print(matrix_1)
print(matrix_2)
print(matrix_1 + matrix_2)
