#!/usr/bin/python3
"""Calcule la quantite d'eau entre des murs representes par un tableau"""


def rain(walls):
    """return how many square units of water will be retained after it rains"""

    index = 0
    waterQuantity = 0
    nbBorne = 0
    wallHeight = 0

    if not walls:
        return 0

    while index < len(walls):
        nbZero = 0

        if ((index == 0 and walls[0] == 0) or 
                (index == len(walls) - 1 and walls[-1] == 0)):
            index += 1
            continue

        while index < len(walls):
            if walls[index] == 0:
                nbZero += 1
                index += 1
            else:
                if nbBorne == 0:
                    wallHeight = walls[index]
                nbBorne += 1

                if nbBorne == 2:
                    secondWall = walls[index]
                    if secondWall < wallHeight:
                        wallHeight = secondWall
                    waterQuantity += wallHeight * nbZero
                    nbBorne = 1
                    wallHeight = secondWall
                    index += 1
                    break
                index += 1

    return waterQuantity
