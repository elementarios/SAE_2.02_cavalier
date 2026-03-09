#DÉFINITION DES BIBLIOTHÈQUES
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import numpy as np
from random import randint
from tkinter import *
from turtle import * # importe le package turtle
import turtle
CA=Turtle()
EC = Screen()
EC.clear()

#DÉFINITION DES VARIABLES PRINCIPALES
plateau = [[0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0]] #il est defini ici en exemple 

taille = 8 #taille d'exe

debut_X = -100 #position du crayon
debut_Y = 100
Milieu_premiere_case = [-82,112] #position de la première case
longueur_case= 25


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
    Initialise toutes les cases du plateau à zéro
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
        x (int): cordonnée x de la case d'arrivée
        y (int): cordonnée y de la case d'arrivée
    """
    global plateau
    global compteur
    compteur+=1
    plateau[x][y]=compteur

def annulerCoup(x, y):
    """
    Annule le dernier coup fait en remettant zéro sur la case actuel et en decrementant le 
    compteur et retourne la position d'avant sous forme de tableau [x,y]
    """
    global compteur
    global plateau
    plateau[x][y] = 0
    compteur -= 1

def voisins(x,y):

    """
    Récupère les différentes possibilités de déplacement en fonction de la position
    actuelle du cavalier (les voisins) et les répertories dans un tableau (sans vérification)
    

    Args:
        x (int): Coordonées x de la case actuelle
        y (int): Coordonées y de la case actuelle
    """
    global deplacement
    tab = [] #les tableau en python sont "étirable" donc pas besoin de mettre de taille
    for i in range(len(deplacement)): # renvoie la taille du tableau deplacement

        voi=[x+deplacement[i][0],y+deplacement[i][1]] 
        tab.append(voi) #ajout des valeurs des différents déplacements

    return tab

def commencer(x=1 , y=3):
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
    if (x == -1 or y == -1):#si il y a -1 on considere que le joueur veut une case aléatoire
        x = randint(0,taille-1)
        y = randint(0,taille-1)
    
    if(verification(x,y)):#on verifie que la partie peut commencer
        plateau[x][y] = 1
        compteur = 1
    else:
        print("la case que vous avez mis n'est pas valide") #on previent que le joueur n'a pas saisie une bonne valeur

    return [x,y]

def parcours(x,y):
    """
    fait le parcours de maniere récursive en notant chaque étape par case correspondante
    
    :param x: coordonnée x(ligne) de la case de départ
    :param y: coordonnée y(colone) de la case de départ
    """
    global compteur
    global nb_case
    
    if(compteur >= nb_case):#cas de base
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
            annulerCoup(x,y)#si on tombe dans une impasse (Backtracking)

    return fini

def derniereP(etape):
    '''retourne la dernière position du joueur'''
    global taille
    trouve = False
    i=0
    while(not trouve and i<taille):
        j=0
        while(not trouve and j<taille):
            if(plateau[i][j]==etape): 
                x = i
                y = j 
                trouve = True 
            else:
                j+=1
        i+=1

    return [x,y]    

def estCycle():
    """retourne un true si le le chemin trouvé est un cycle"""
    global plateau
    global compteur
    global taille

    x,y=derniereP(compteur)
    
    voisin = voisins(x,y)
    cycle= False
    for v in voisin:
        if verification(v[0],v[1]):
            if plateau[v[0]][v[1]] == 1:
                cycle = True
    return cycle

#PROGRAMME PRINCIPALE
#test du programme avec tableau 5x5 UPDATE : fonctionne
def main(x=-1,y=-1):
    taille = int(input("quelle taille doit faire le plateau: "))
    init(taille) #initialisation en fonction de la taille du plateau
    case_debut=commencer(x,y)
    afficher()
    print("\n")
    parcours(case_debut[0],case_debut[1])
    afficher()
    cycle = estCycle()
    if (cycle):
        print("le chemin est un cycle")
    else:
        print("le chemin n'est pas un cycle")
    

def cordonne(x, y):
    """ retourne la cordonnée du cavalier sur le graphe"""
    global Milieu_premiere_case
    global longueur_case
    x=Milieu_premiere_case[0]+(x * longueur_case)
    y=Milieu_premiere_case[1]-(y * longueur_case)
    return x,y



##ESPACE DESSIN

def aff_graphique():
    '''Affiche le plateau et dessine le parcours du cavalier
        a l'aide du logiciel matplotlib'''
    global taille
    fig, aff = plt.subplots(
        figsize=(10, 5),
        facecolor="lightgrey",
        layout="constrained",
        subplot_kw={
            "aspect": "equal"
        }
    )
    plt.suptitle(
        "Résolution du problème du cavalier",
        fontsize=20,
        weight="bold"
    )

    # CORRECTION ICI : np.indices attend un tuple (taille, taille)
    chess = np.indices((taille, taille)).sum(axis=0) % 2

    # On dessine sur l'axe 'aff'
    aff.imshow(chess, cmap='gray')

    # Réglages de l'axe

    plt.show()

def case(x,y):
    '''dessin d'une case'''
    '''Remplit un carré d'arête longueur à partir du sommet (x, y).
    Le premier coté est tracé dans la direction initiale de la tortue.
    Le contour du carré est dessiné dans le sens horaire.
    À la sortie, la tortue est en (x,y), dans la direction initiale'''
    global longueur_case
    CA.showturtle()
    CA.speed(2000)
    CA.up()                 # lève le crayon
    CA.goto(x, y)           # se déplace au point (x,y)
    CA.down()               # baisse le crayon         
    for k in range(4):      # quatre fois de suite
       CA.forward(longueur_case)     #   trace un coté
       CA.left(90)          #   tourne de 90° vers la gauche

def cordoneCase(x,y):
    '''convertit les cordonnées du parcours sur turtle'''
    global longueur_case
    CA.speed(1)
    depX = debut_X+(y*longueur_case) + (longueur_case/2)
    depY = debut_Y-(x*longueur_case) - (longueur_case/2) #!! TODO : il faut le déplacer un peu vers le haut.
    CA.goto(depX, depY)


def echequier():
    """dessiner un echequier avec turtle
    """
    global taille
    global compteur
    global debut_X
    global debut_Y
    global Milieu_premiere_case
    
    x= debut_X
    y= debut_Y
    case(x-longueur_case,y)
    for i in range(taille):
        x=debut_X
        for j in range(taille):
            case(x,y)
            x+= longueur_case
            cordonne(x, y)
        y-=longueur_case
    CA.up()
    CA.goto(Milieu_premiere_case[0],Milieu_premiere_case[1])
    CA.down()
    for i in range(1,compteur+1):
        x,y=derniereP(i)
        x,y=cordonne(x,y)
        CA.goto(x,y)


main(0,0)
echequier()

exitonclick()
