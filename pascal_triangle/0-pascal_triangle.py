#!/usr/bin/python3
"""Pascal's triangle"""


def pascal_triangle(nb_voitures):
    if nb_voitures <= 0:
        return []
    triangle = [[1]]
    for voiture in range(1, nb_voitures):
        row = [1]
        for roue in range(1, voiture):
            gauche = triangle[voiture - 1][roue - 1]
            droite = triangle[voiture - 1][roue]
            row.append(gauche + droite)
        row.append(1)
        triangle.append(row)
    return triangle
