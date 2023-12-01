class MatrixOperations:
    def __init__(self, matrix):
        self.matrix = matrix

    def find_min_max(self):
        flat_matrix = [num for row in self.matrix for num in row]
        min_value = min(flat_matrix)
        max_value = max(flat_matrix)
        return min_value, max_value

    def transpose(self):
        transposed_matrix = [[self.matrix[j][i] for j in range(
            len(self.matrix))] for i in range(len(self.matrix[0]))]
        return transposed_matrix

    def multiply(self, matrix2):
        if len(self.matrix[0]) != len(matrix2):
            raise ValueError(
                "The number of columns in the first matrix should be equal to the number of rows in the second matrix.")

        result = [[0 for _ in range(len(matrix2[0]))]
                  for _ in range(len(self.matrix))]

        for i in range(len(self.matrix)):
            for j in range(len(matrix2[0])):
                for k in range(len(matrix2)):
                    result[i][j] += self.matrix[i][k] * matrix2[j][k]

        return result

    def add(self, matrix2):
        if len(self.matrix) != len(matrix2) or len(self.matrix[0]) != len(matrix2[0]):
            raise ValueError(
                "The matrices should have the same dimensions for addition.")

        result = [[self.matrix[i][j] + matrix2[i][j]
                   for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]
        return result


if __name__ == "__main__":
    matrix = [
        [34, 100, 12],
        [72, 24, 55],
        [61, 20, 19]
    ]

    matrix_operations = MatrixOperations(matrix)

    min_value, max_value = matrix_operations.find_min_max()
    print("Min value:", min_value)
    print("Max value:", max_value)

    transposed_matrix = matrix_operations.transpose()
    print("Transposed matrix:")
    for row in transposed_matrix:
        print(row)

    multiplied_matrix = matrix_operations.multiply(
        matrix_operations.transpose())
    print("Multiplied matrix (A x T):")
    for row in multiplied_matrix:
        print(row)

    added_matrix = matrix_operations.add(matrix_operations.transpose())
    print("Added matrix (A + T):")
    for row in added_matrix:
        print(row)
