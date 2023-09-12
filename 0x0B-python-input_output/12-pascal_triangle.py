#!/usr/bin/env python3
"""
Defines Pascal's Triangle that creates a list of lists.
"""

def generate_pascals_triangle(n):
    """
    Generates Pascal's Triangle up to the nth row.

    :param n: The number of rows to generate.
    :return: A list of lists representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = []
    previous_row = []

    for i in range(n):
        current_row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                current_row.append(1)
            else:
                current_row.append(previous_row[j - 1] + previous_row[j])
        triangle.append(current_row)
        previous_row = current_row

    return triangle

if __name__ == "__main__":
    n = int(input("Enter the number of rows for Pascal's Triangle: "))
    pascal_triangle = generate_pascals_triangle(n)
    
    print("Pascal's Triangle:")
    for row in pascal_triangle:
        print(row)

