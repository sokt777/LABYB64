def row_sums(matrix):
    if not matrix:
        return []
    return [sum(row) for row in matrix]


def column_sums(matrix):
    if not matrix:
        return []
    columns = len(matrix[0])
    return [sum(matrix[row][col] for row in range(len(matrix)))
            for col in range(columns)]


def diagonal_pattern(size):
    result = []
    for row in range(size):
        new_row = []
        for col in range(size):
            if row == col:
                new_row.append(0)
            elif row < col:
                new_row.append(1)
            else:
                new_row.append(2)
        result.append(new_row)
    return result

def transform(matrix)
    if not matrix:
        return []
    new_matrix = []
    for row in matrix:
        new_row = []
        for value in row:
            if value > 0:
                new_row.append(value + 5)
            else:
                new_row.append(value)
        new_matrix.append(new_row)
    return new_matrix