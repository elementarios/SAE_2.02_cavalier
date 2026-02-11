from matplotlib import pylab as plt
from random import randint


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

def ajoutDeDeplacement(x,y):
    """modifie le plateau pour ajouter un deplacement

    Args:
        x (int): cordonnée x de l'arrivée
        y (int): cordonnée y de l'arrivée
    """
    global plateau
    global compteur
    global deplacement
    depX = deplacement[rand][1]
    depY = deplacement[rand][2] #il se passe comment le choix des déplacements ?
    if (verification(x+depX, y+depY)):
        x += depX
        y += depY



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
        #x = xDeb
        #y = yDeb #Le cas 2 dans le cas ou l'on doit passer de la dernière case à la première
        fini = True #on peut faire un return vide pour arreter la fonction
    
    else:
        fini = False
        i=0
        voisin=voisins(x,y)

        while(not fini and i < len(voisin)):
            x1,y1=voisin[i][0],voisin[i][1] #une double assignation

            if(verification(x1,y1)):
                ajoutDeDeplacement(x1,y1)
                fini = parcours(x1,y1)#cas récusrif

            i+=1 #le i++ n'existe pas on fait i+=1 qui vaut i=i+1
        
        if(not fini):
            annulerCoup()#si on tombe dans une impasse (Backtracking)

    return fini

def voisins(x,y):

    """retourne un tableau des voisin (sans verification) dans le style [[x,y][x,y]]

    Args:
        x (int): Coordonées x de la case
        y (int): Coordonées y de la case
    """
    global deplacement
    tab = [] #les tableau en python sont "étirable" donc pas besoin de mettre de taille
    for i in range(len(deplacement)):

        voi=[x+deplacement[i][0],y+deplacement[i][1]]
        tab.append(voi) #on rajoute a la fin du tableau

    return tab

#def dessiner_chemin(x, y):
    #dessiner le programme via console ou graphique (matplotlib peut-être)


def estCycle():
    """retourne un true si le le chemin trouvé est un cycle"""
    global plateau
    global compteur
    global taille
    i = 0
    trouver = False

    while(not trouver and i < taille):
        j = 0
        while(not trouver and j < taille):
            if(plateau[i][j]==compteur):
                x= i
                y= j
                trouver = True
            else:
                j+=1
        i+=1
    
    voisin = voisins(x,y)
    cycle= False
    for v in voisin:
        if(plateau[v[0]][v[1]]==1):
            cycle = True
    return cycle


def commencer(x=-1 , y=-1):
    """permet d'initialiser le debut de la partie et retourne 
    les coordonnées de la case de début sous la forme [x,y]
    si aucune case n'est donnée alors elle sera choisis aléatoirement

    Args:
        x (int, optional): coordonnées X de la case. Defaults to -1.
        y (int, optional): coordonnées Y de la case. Defaults to -1.
    """
    global plateau
    global taille
    global compteur
    if (x == -1 and y ==-1):
        x = randint(0,taille-1)
        y = randint(0,taille-1)
    
    plateau[x][y] = 1
    compteur = 1

    return [x,y]



#PROGRAMME PRINCIPALE
#test du programme avec tableau 5x5
init(taille) #initialisation en fonction de la taille du plateau

afficher()

tab=voisins(5,6)
print(tab)