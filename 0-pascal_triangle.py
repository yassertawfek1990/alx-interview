def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        # Initialize a row with 1s
        row = [1] * (i + 1)

        # Update the values for the current row based on the previous row
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        # Add the current row to the triangle
        triangle.append(row)

    return triangle


if __name__ == "__main__":
    def print_triangle(triangle):
        """
        Print the triangle
        """
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))

    print_triangle(pascal_triangle(5))
