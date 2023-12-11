#!/usr/bin/python3
"""Calcule la quantite d'eau retenue entre des murs representes par un tableau."""

def rain(walls):
    """return how many square units of water will be retained after it rains"""
    
    index = 0
    waterQuantity = 0
    nbBorne = 0
    wallHeight = 0

    # Si le tableau est vide, aucune eau ne peut etre retenue
    if not walls:
        return 0

    # Parcours du tableau des murs
    while index < len(walls):
        nbZero = 0

        # Ignorer les zéros aux extremites du tableau
        if (index == 0 and walls[0] == 0) or (index == len(walls) - 1 and walls[-1] == 0):
            index += 1
            continue

        # Recherche de sequences de zeros entre les murs
        while index < len(walls):
            if walls[index] == 0:
                nbZero += 1
                index += 1
            else:
                # Enregistrement de la hauteur du mur si c'est la premiere borne
                if nbBorne == 0:
                    wallHeight = walls[index]
                nbBorne += 1

                # Si la deuxieme borne est trouvee, calcul de la quantite d'eau retenue
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
