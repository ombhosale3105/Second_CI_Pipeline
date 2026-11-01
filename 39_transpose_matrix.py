def transpose_matrix(matrix: list[list]) -> list[list]:
    """Return the transpose of a rectangular matrix; an empty matrix returns []."""
    if not matrix:
        return []
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError("All rows must have the same number of columns")
    return [list(column) for column in zip(*matrix)]


if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    matrix = []
    for row_index in range(rows):
        matrix.append(list(map(int, input(f"Enter row {row_index + 1}: ").split())))
    print("Transposed matrix:")
    for row in transpose_matrix(matrix):
        print(*row)
