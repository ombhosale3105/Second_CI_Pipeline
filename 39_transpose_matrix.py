def transpose_matrix(matrix: list[list]) -> list[list]:
    """Return the transpose of a rectangular matrix."""
    if not matrix:
        return []
    return [list(row) for row in zip(*matrix)]


if __name__ == "__main__":
    rows = int(input("Number of rows: "))
    matrix = []
    for row_index in range(rows):
        row = input(f"Enter row {row_index + 1} values separated by spaces: ")
        matrix.append([int(value) for value in row.split()])
    print(transpose_matrix(matrix))
