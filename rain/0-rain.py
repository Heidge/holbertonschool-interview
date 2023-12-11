#!/usr/bin/python3

def rain(walls):
    """
    Calcule la quantit� d'eau retenue entre des murs repr�sent�s par un tableau.

    Parameters:
    walls (list): Un tableau repr�sentant la hauteur des murs.

    Returns:
    int: La quantit� totale d'eau retenue entre les murs.
    """

    # Initialisation des variables
    index = 0
    waterQuantity = 0
    nbBorne = 0
    wallHeight = 0

    # Si le tableau est vide, aucune eau ne peut �tre retenue
    if len(walls) == 0:
        return 0

    # Parcours du tableau des murs
    while index < len(walls):
        nbZero = 0

        # Ignorer les z�ros aux extr�mit�s du tableau
        if (index == 0 and walls[0] == 0) or (index == len(walls) - 1 and walls[len(walls) - 1] == 0):
            index += 1
            pass

        # Recherche de s�quences de z�ros entre les murs
        while index < len(walls):
            if walls[index] == 0:
                nbZero += 1
                index += 1
            else:
                # Enregistrement de la hauteur du mur si c'est la premi�re borne
                if nbBorne == 0:
                    wallHeight = walls[index]
                nbBorne += 1

                # Si la deuxi�me borne est trouv�e, calcul de la quantit� d'eau retenue
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
