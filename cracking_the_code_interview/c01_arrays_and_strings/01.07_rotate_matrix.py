# Problem: Rotate Matrix
# Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place? 


# O(n * n)
def rotate_matrix(matrix):
    n = len(matrix)
    rotated = []
    for row in range(n):
        rotated.append([])
        for i in range(n - 1, -1, -1):
            rotated[row].append(matrix[i][row])
    return rotated


# O(n * n) but in-place
def rotate_matrix_in_place(matrix):
    n = len(matrix)
    # We go through the matrix by concentric layers.
    # We substitute the top-left cell by the bottom-left cell
    # The bottom-left cell by the bottom-right cell
    # The bottom-right cell by the top-right cell
    # The top-right cell by the top-left-cell

    for layer in range(len(matrix) // 2):
        for col in range(layer, (n - layer - 1)):
            aux = matrix[layer][col]
            matrix[layer][col] = matrix[n - 1 - col][layer]
            matrix[n - 1 - col][layer] = matrix[n - 1 - layer][n - 1 - col]
            matrix[n - 1 - layer][n - 1 - col] = matrix[col][n - 1 - layer]
            matrix[col][n - 1 - layer] = aux
    return matrix
