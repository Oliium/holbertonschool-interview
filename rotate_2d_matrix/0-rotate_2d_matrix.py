#!/usr/bin/python3
"""Rotate a 2D matrix 90 degrees clockwise, in place."""


def rotate_2d_matrix(matrix):
    """Rotate an n x n 2D matrix 90 degrees clockwise in place.

    Args:
        matrix: n x n list of lists. Modified in place; returns nothing.
    """
    n = len(matrix)

    # Transpose the matrix (swap across the main diagonal).
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row to complete the clockwise rotation.
    for row in matrix:
        row.reverse()
