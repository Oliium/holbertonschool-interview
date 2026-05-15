#!/usr/bin/python3
"""Le Triangle Pascal"""


def pascal_triangle(nb_voitures):
    """Retourne une liste de listes représentant le triangle de Pascal de n."""
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
