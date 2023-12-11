#!/usr/bin/python3

def rain(walls):
    index = 0
    waterQuantity = 0
    nbBorne = 0
    wallHeight = 0
    
    if len(walls) == 0:
        return 0
    
    while index < len(walls):
        nbZero = 0
 
        if index == 0 and walls[0] == 0 or index == len(walls) - 1 and walls[len(walls) - 1] == 0:
            index += 1
            pass
        
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
                    index+=1
                    break
                index += 1

            
    return waterQuantity
            
