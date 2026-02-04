
plateau = [[0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0]] #il est defini ici en exemple 

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
    global taille #global permet d'appeler la variable global et pas avoir une ambiguité
    global plateau
    Xvalide = x > -1 and x < taille
    Yvalide = y > -1 and y < taille
    return Xvalide and Yvalide and plateau[x][y]==0

assert verification(0,0) == True , verification(0,0) #c'est un test unitaire qui bloque si il est faux
assert verification(-1,1) == False , verification(-1,1)


def init(Ntaille):
    """
    Docstring for créetableau
    
    :param taille: Description
    """
    global plateau 
    global taille
    global compteur
    global nb_case

    taille = Ntaille
    compteur = 0
    nb_case = taille*taille
    plateau = [[0 for i in range(taille)]for j in range(taille)] #on crée le tableau en compréhension


def afficher():
    """affiche le plateau de maniere "classe"
    """
    global plateau
    global taille
    for i in range(taille):
        ligne=""
        for j in range(taille):
            ligne+=str(plateau[i][j])+" " #la commande str transforme en string 
        print(ligne)

init(8)
afficher()

def ajoutDeDeplacement(x,y):
    """modifie le plateau pour ajouter un deplacement

    Args:
        x (int): cordonnée x de l'arrivée
        y (int): cordonnée y de l'arrivée
    """
    global plateau
    global compteur


def annulerCoup():
    """
    Annule le dernier coup fait en remettant zéro sur la case actuel et en decrementant compteur
    et retourne la position d'avant sous forme de tableau [x,y]
    """


def parcours(x,y):
    """
    fait le parcour de maniere récursive en mettant en notant sur la case chaque étape
    
    :param x: coordonnée x de la case de départ
    :param y: coordonnée y de la case d'arrivée
    """
    global compteur
    global nb_case
    if(compteur >= nb_case):#cas de base
        return None #on peut faire un return vide pour arreter la fonction
    else:
        return None #None a virer
                    #il faut qu'on fasse un appelle recursive pour chaque mouvement

                    #le probleme est de savoir quand un chemin mene a une impasse