
plateau = [[0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0]] #il est defini ici en exemple mais on pourrais crée une fonction a coté

taille = 8

compteur = 0 #le nombre de déplacement effectué
nb_case = 0 #elle sera definit plus tard


deplacement = [[1,2],
               [-1,2],
               [1,-2],
               [-1,-2],
               [2,1],
               [2,-1],
               [-2,1],
               [-2,-1]] #tableau recensent tout les déplacement possibles


def verification(x:int,y:int):
    """verifie si la case rentre en parametre est valide et retourne un booléen

    Args:
        x (int): cordonnées X d'une case
        y (int): cordonnées Y d'une case
    """
    global taille
    global plateau
    Xvalide = x > -1 and x < taille
    Yvalide = y > -1 and y < taille
    return Xvalide and Yvalide and plateau[x][y]==0

assert verification(0,0) == True , verification(0,0)
assert verification(-1,1) == False , verification(-1,1)


def créetableau(Ntaille):
    """
    Docstring for créetableau
    
    :param taille: Description
    """
    global plateau
    global taille
    taille = Ntaille
    plateau = [[0 for i in range(taille)]for j in range(taille)]

créetableau(5)
print(plateau)

