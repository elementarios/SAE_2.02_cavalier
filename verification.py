
plateau = [[0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0]] #il est defini ici en exemple 

taille = 8 #Définit ici comme une constante symbolique

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

#Permet d'observer si une case de [x,y] n'a pas été visité. 
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

#Initialisation de l'échiquier (taille, compteur, nb_case)
def init(Ntaille, x, y):
    """
    Docstring for créetableau
    
    :param taille: Description
    """
    global plateau #appels des variables du programme principale
    global taille
    global compteur
    global nb_case

    taille = Ntaille
    compteur = 0
    nb_case = taille*taille #définition de la taille du plateau
    plateau = [[0 for i in range(taille)]for j in range(taille)] #on crée le tableau en compréhension
    plateau[x][y] = 1 #nous initialisons le premier sommet de l'échiquier à 1


def afficher():
    """affiche le plateau de maniere "classe"
    """
    global plateau
    global taille
    for i in range(taille): #taille = 8
        ligne="" #affichage de la chaine tab dans un string (comme la méthode java)
        for j in range(taille):
            #str transforme la case du tableau en chaine de caractères
            ligne+=str(plateau[i][j])+" " #la commande str transforme en string 
        print(ligne)

def ajoutDeDeplacement(x,y):
    """modifie le plateau pour ajouter un deplacement

    Args:
        x (int): cordonnée x de l'arrivée
        y (int): cordonnée y de l'arrivée
    """
    global plateau
    global compteur
    #ici il faudrait faire un rand du tableau des déplacements ?

    


def annulerCoup(x, y):
    """
    Annule le dernier coup fait en remettant zéro sur la case actuel et en decrementant compteur
    et retourne la position d'avant sous forme de tableau [x,y]
    """
    global compteur
    global plateau
    plateau[x][y] = 0
    compteur -= 1
    verifx = 0
    verify = 0
    while(plateau[verifx][verify] != compteur and verifx < taille):
       while(plateau[verifx][verify] != compteur and verify < taille): 
        if (plateau[verifx][verify] == compteur):
            x = verifx
            y = verify

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
        if (verification(x,y)):
            ajoutDeDeplacement(x,y)
            compteur += 1
            parcours(x,y)
        else:
            nb_case = 0
                    #None a virer
                    #il faut qu'on fasse un appelle recursive pour chaque mouvement

                    #le probleme est de savoir quand un chemin mene a une impasse


#PROGRAMME PRINCIPALE
if ((taille % 2) == 0) :
    x = taille / 2 #nous faisons spawn le cavalier au milieu de l'échiquier
    y = taille / 2
else:
    x = (taille % 2) + 1
    y = taille % 2 # il faudra coder une fonction qui pose aléatiorement le pion

init(taille, x, y) #initialisation en fonction de la taille du plateau

afficher()