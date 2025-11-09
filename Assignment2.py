# Function 1: Lists - Finding the Maximum and Second Maximum in a List
# This function takes a list of numbers as input and returns the maximum and second maximum values.
def max_two_in_list(numbers):

    if not numbers:
        return (None, None)

    if len(numbers) == 1:
        return (numbers[0], None)

    max1 = numbers[0]
    max2 = None

    for x in numbers[1:]:
        if x > max1:
            max2 = max1
            max1 = x
        elif x != max1 and (max2 is None or x > max2):
            max2 = x

    return (max1, max2)


# Function 2: Lists - Removing Duplicates and Sorting
# This function takes a list of numbers and returns a sorted list with duplicates removed.
def remove_duplicates_and_sort(numbers):

    unique_sorted = sorted(set(numbers))
    return unique_sorted


# Function 3: Single-Dimensional Arrays - Cumulative Sum
# This function takes an array (list) of numbers and returns a new list where each element is the cumulative sum of the previous elements.
def cumulative_sum(arr):

    result = []
    total = 0
    for num in arr:
        total += num          
        result.append(total)  
    return result

# Function 4: Two-Dimensional Arrays - Matrix Transpose
# This function takes a 2D list (matrix) and returns its transpose.
def transpose_matrix(matrix):

    if not matrix:
        return []

    transposed = [list(row) for row in zip(*matrix)]
    return transposed

# Function 5: Slicing - Extracting Every Nth Element
# This function takes a list and a step value N and returns every Nth element.
def slice_every_nth(lst, step):

    if step <= 0:
        return []  
    return lst[::step]

# Function 6: Arithmetic Operations with Arrays - Dot Product
# This function takes two lists of the same length and returns their dot product.
def dot_product(list1, list2):

    if len(list1) != len(list2):
        return None  
    total = 0
    for a, b in zip(list1, list2):
        total += a * b
    return total

# Function 7: Arithmetic Operations with Arrays - Matrix Multiplication
# This function takes two 2D lists (matrices) and returns their matrix product.
def matrix_multiplication(matrix1, matrix2):
    # Check if multiplication is possible
    if not matrix1 or not matrix2 or len(matrix1[0]) != len(matrix2):
        return []  

    rows_matrix1 = len(matrix1)
    cols_matrix2 = len(matrix2[0])
    cols_matrix1 = len(matrix1[0])

    result = [[0 for _ in range(cols_matrix2)] for _ in range(rows_matrix1)]

    for i in range(rows_matrix1):
        for j in range(cols_matrix2):
            for k in range(cols_matrix1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result