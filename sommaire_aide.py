# ============================================================================
# SOMMAIRE COMPLET DES FONCTIONNALITÉS ET UTILISATIONS DE PYTHON
# Guide pédagogique pour étudiants en informatique
# ============================================================================

# ============================================================================
# 1. VARIABLES ET TYPES DE DONNÉES
# ============================================================================

# Les variables en Python peuvent changer de type dynamiquement
x = 7              # Entier (int)
x = 8              # Toujours x, mais valeur changée
x = 7.4            # Flottant (float)
x = True           # Booléen (bool) - Note: Majuscule requise
x = "name"         # Chaîne de caractères (str)
x = [1, 2, 3]      # Liste (list)
x = (1, 2, 3)      # Tuple (tuple) - immuable
x = {1, 2, 3}      # Ensemble (set)
x = {"clé": "valeur"}  # Dictionnaire (dict)

# En Python, une variable peut changer de type à tout moment
# (contrairement au C qui est typé statiquement)

# Vérifier le type d'une variable
type(x)            # Affiche <class '...'>

# Conversion de types (cast)
int("42")          # Convertit string en int
float("3.14")      # Convertit string en float
str(42)            # Convertit int en string
list((1, 2, 3))    # Convertit tuple en liste

# ============================================================================
# 2. ENTRÉE/SORTIE (INPUT/OUTPUT)
# ============================================================================

# Lecture au clavier - input() retourne toujours une chaîne de caractères
nom = input("Entrez votre nom: ")

# Conversion nécessaire pour les nombres
age = int(input("Entrez votre âge: "))
prix = float(input("Entrez le prix: "))

# Affichage à l'écran - print()
print("Bonjour", nom)
print("Vous avez", age, "ans")

# Affichage avec formatage
print(f"Je m'appelle {nom} et j'ai {age} ans")  # f-string (recommandé)
print("Bonjour {} et {}".format(nom, age))      # Ancienne méthode
print("Bonjour %s et %d" % (nom, age))          # Très ancienne méthode

# Affichage sans retour à la ligne
print("Texte 1", end=" ")
print("Texte 2")  # Affiche: Texte 1 Texte 2

# ============================================================================
# 3. OPÉRATEURS ARITHMÉTIQUES
# ============================================================================

# Opérations mathématiques de base
addition = 5 + 3        # 8
soustraction = 5 - 3    # 2
multiplication = 5 * 3  # 15
division = 5 / 3        # 1.666... (division réelle, retourne float)
division_entiere = 5 // 3  # 1 (division entière, retourne int)
reste = 5 % 3           # 2 (modulo)
puissance = 5 ** 3      # 125 (exponentiation)

# Opérateurs composés (raccourcis)
x = 10
x += 5      # x = x + 5  (x vaut 15)
x -= 3      # x = x - 3
x *= 2      # x = x * 2
x /= 4      # x = x / 4
x //= 2     # x = x // 2
x %= 3      # x = x % 3

# ============================================================================
# 4. OPÉRATEURS DE COMPARAISON
# ============================================================================

5 == 3      # False (égal à)
5 != 3      # True (différent de)
5 > 3       # True (supérieur à)
5 >= 3      # True (supérieur ou égal)
5 < 3       # False (inférieur à)
5 <= 3      # False (inférieur ou égal)

# Comparaison de chaînes (ordre alphabétique)
"abc" < "def"   # True

# ============================================================================
# 5. OPÉRATEURS LOGIQUES
# ============================================================================

# ET logique (AND)
(5 > 3) and (2 < 4)     # True
(5 > 3) and (2 > 4)     # False

# OU logique (OR)
(5 > 3) or (2 > 4)      # True
(5 < 3) or (2 > 4)      # False

# NON logique (NOT)
not (5 > 3)             # False
not (5 < 3)             # True

# ============================================================================
# 6. CONDITIONS (IF/ELIF/ELSE)
# ============================================================================

# Structure de base - ATTENTION à l'indentation (obligatoire en Python)
age = 20

if age >= 18:
    print("Vous êtes majeur")
elif age >= 13:
    print("Vous êtes adolescent")
else:
    print("Vous êtes enfant")

# Condition ternaire (opérateur conditionnel)
statut = "Majeur" if age >= 18 else "Mineur"

# Condition avec plusieurs conditions
if age >= 18 and age <= 65:
    print("Vous êtes en âge de travailler")

# ============================================================================
# 7. BOUCLES - WHILE (Tant que)
# ============================================================================

# Boucle tant que la condition est vraie
compteur = 0
while compteur < 5:
    print(f"Compteur: {compteur}")
    compteur += 1

# Exemple: Lecture jusqu'à condition d'arrêt
reponse = ""
while reponse != "oui":
    reponse = input("Voulez-vous continuer? (oui/non): ")

# Sortie de boucle avec break
while True:
    choix = input("Entrez 'quitter' pour arrêter: ")
    if choix == "quitter":
        break
    print(f"Vous avez dit: {choix}")

# Sauter une itération avec continue
compteur = 0
while compteur < 10:
    compteur += 1
    if compteur % 2 == 0:
        continue  # Saute les nombres pairs
    print(f"Nombre impair: {compteur}")

# ============================================================================
# 8. BOUCLES - FOR (Pour chaque)
# ============================================================================

# Boucle for simple (itération)
for i in range(5):  # range(5) = 0, 1, 2, 3, 4
    print(f"i = {i}")

# range avec début et fin
for i in range(1, 6):       # 1, 2, 3, 4, 5 (fin non incluse)
    print(i)

# range avec pas
for i in range(0, 10, 2):   # 0, 2, 4, 6, 8 (pas de 2)
    print(i)

# range décroissant
for i in range(10, 0, -1):  # 10, 9, 8, ..., 1
    print(i)

# Itération sur une liste
fruits = ["pomme", "banane", "orange"]
for fruit in fruits:
    print(f"Fruit: {fruit}")

# Itération avec indice (enumerate)
for indice, fruit in enumerate(fruits):
    print(f"Position {indice}: {fruit}")

# Boucle for imbriquée (tables de multiplication)
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")

# ============================================================================
# 9. LISTES (TABLEAUX DYNAMIQUES)
# ============================================================================

# Créer une liste
nombres = [1, 2, 3, 4, 5]
mixte = [1, "texte", 3.14, True]
vide = []

# Accéder aux éléments (indexation commence à 0)
print(nombres[0])       # 1
print(nombres[-1])      # 5 (dernier élément)
print(nombres[-2])      # 4 (avant-dernier)

# Tranches (slicing) - extraction de sous-listes
print(nombres[1:4])     # [2, 3, 4] (indices 1, 2, 3)
print(nombres[:3])      # [1, 2, 3] (du début jusqu'à index 3)
print(nombres[2:])      # [3, 4, 5] (de l'index 2 à la fin)
print(nombres[::2])     # [1, 3, 5] (tous les 2 éléments)
print(nombres[::-1])    # [5, 4, 3, 2, 1] (inverse la liste)

# Ajouter des éléments
nombres.append(6)       # Ajoute 6 à la fin
nombres.insert(0, 0)    # Insère 0 à l'index 0
nombres.extend([7, 8])  # Ajoute une liste

# Supprimer des éléments
nombres.remove(2)       # Supprime la première occurrence de 2
nombres.pop()           # Supprime et retourne le dernier
nombres.pop(0)          # Supprime et retourne l'élément à l'index 0
del nombres[1]          # Supprime l'élément à l'index 1

# Rechercher dans une liste
if 5 in nombres:
    print("5 est dans la liste")
    index = nombres.index(5)  # Retourne l'index de 5

# Longueur d'une liste
taille = len(nombres)

# Trier une liste
nombres.sort()          # Trie sur place
nombres.sort(reverse=True)  # Trie en ordre décroissant
sorted(nombres)         # Retourne une nouvelle liste triée

# Copier une liste
copie = nombres.copy()  # Ou: copie = nombres[:] ou copie = list(nombres)

# Compter les occurrences
occurrences = nombres.count(2)

# ============================================================================
# 10. TUPLES (LISTES IMMUABLES)
# ============================================================================

# Créer un tuple
coordonnees = (10, 20)
point_3d = (10, 20, 30)
vide = ()

# Un tuple avec un élément nécessite une virgule
singleton = (5,)

# Accéder aux éléments (comme une liste)
print(coordonnees[0])   # 10

# Les tuples ne peuvent pas être modifiés (immuables)
# coordonnees[0] = 100  # ERREUR!

# Les tuples sont plus rapides que les listes
# Utilisez des tuples quand vous ne voulez pas modifier les données

# Dépaquetage (unpacking)
x, y = coordonnees      # x=10, y=20
a, b, c = point_3d      # a=10, b=20, c=30

# ============================================================================
# 11. DICTIONNAIRES (ASSOCIATIFS/CLÉS-VALEURS)
# ============================================================================

# Créer un dictionnaire
personne = {"nom": "Dupont", "age": 25, "ville": "Paris"}
vide = {}

# Accéder aux valeurs
print(personne["nom"])      # "Dupont"

# Accéder avec protection (si clé n'existe pas)
print(personne.get("nom"))          # "Dupont"
print(personne.get("metier", ""))   # "" (valeur par défaut)

# Ajouter/modifier des éléments
personne["metier"] = "Informaticien"
personne["age"] = 26

# Vérifier si une clé existe
if "nom" in personne:
    print("La clé 'nom' existe")

# Supprimer une clé-valeur
del personne["ville"]
personne.pop("metier")

# Itérer sur les clés
for cle in personne:
    print(f"{cle}: {personne[cle]}")

# Itérer sur les clés-valeurs
for cle, valeur in personne.items():
    print(f"{cle}: {valeur}")

# Récupérer les clés et valeurs
cles = personne.keys()
valeurs = personne.values()

# Nombre d'éléments
taille = len(personne)

# Dictionnaire imbriqué
employes = {
    "emp1": {"nom": "Alice", "age": 30},
    "emp2": {"nom": "Bob", "age": 25}
}
print(employes["emp1"]["nom"])  # "Alice"

# ============================================================================
# 12. ENSEMBLES (SETS)
# ============================================================================

# Créer un ensemble
nombres = {1, 2, 3, 4, 5}
ensemble_vide = set()  # {} crée un dictionnaire vide!

# Ajouter un élément
nombres.add(6)

# Supprimer un élément
nombres.remove(3)           # Erreur si l'élément n'existe pas
nombres.discard(10)         # Pas d'erreur si absent

# Longueur
taille = len(nombres)

# Vérifier l'appartenance
if 2 in nombres:
    print("2 est dans l'ensemble")

# Opérations sur les ensembles
a = {1, 2, 3}
b = {2, 3, 4}
union = a | b           # {1, 2, 3, 4}
intersection = a & b    # {2, 3}
difference = a - b      # {1}

# ============================================================================
# 13. FONCTIONS (PROCÉDURES)
# ============================================================================

# Fonction simple sans paramètres
def saluer():
    print("Bonjour!")

saluer()  # Appel de la fonction

# Fonction avec paramètres
def saluer_quelqu_un(nom):
    print(f"Bonjour {nom}!")

saluer_quelqu_un("Alice")

# Fonction avec plusieurs paramètres
def additionner(a, b):
    return a + b

resultat = additionner(5, 3)  # resultat = 8

# Paramètres avec valeurs par défaut
def puissance(base, exposant=2):
    return base ** exposant

print(puissance(3))      # 9 (3^2)
print(puissance(3, 3))   # 27 (3^3)

# Arguments nommés (keyword arguments)
print(puissance(exposant=4, base=2))  # 16

# Nombre variable d'arguments
def somme_tous(*nombres):
    total = 0
    for nombre in nombres:
        total += nombre
    return total

print(somme_tous(1, 2, 3, 4, 5))  # 15

# Arguments clés-valeurs variables
def afficher_infos(**infos):
    for cle, valeur in infos.items():
        print(f"{cle}: {valeur}")

afficher_infos(nom="Alice", age=30, ville="Paris")

# Retourner plusieurs valeurs
def calculs(a, b):
    return a + b, a - b, a * b

somme, difference, produit = calculs(10, 3)

# Fonction récursive (qui s'appelle elle-même)
def factorielle(n):
    if n <= 1:
        return 1
    else:
        return n * factorielle(n - 1)

print(factorielle(5))  # 120

# ============================================================================
# 14. PILES (STACKS) - LIFO (Last In, First Out)
# ============================================================================

# En Python, on peut utiliser une liste comme pile
pile = []

# Empiler (push) - ajouter un élément au sommet
pile.append(1)
pile.append(2)
pile.append(3)

# Dépiler (pop) - retirer et retourner le sommet
sommet = pile.pop()     # 3
sommet = pile.pop()     # 2

# Vérifier si la pile est vide
if len(pile) == 0:
    print("Pile vide")

# Consulter le sommet sans dépiler
if len(pile) > 0:
    sommet = pile[-1]   # 1

# Utiliser un deque pour une pile plus efficace
from collections import deque
pile_efficace = deque()
pile_efficace.append(1)      # Empiler
pile_efficace.append(2)
valeur = pile_efficace.pop() # Dépiler

# ============================================================================
# 15. FILES D'ATTENTE (QUEUES) - FIFO (First In, First Out)
# ============================================================================

# Avec une liste (moins efficace)
file = []
file.append(1)              # Enfiler à la fin
file.append(2)
file.append(3)
premier = file.pop(0)       # Défiler du début

# Avec deque (recommandé - plus efficace)
from collections import deque
file_attente = deque()
file_attente.append(1)          # Enfiler
file_attente.append(2)
premier = file_attente.popleft() # Défiler

# Vérifier si vide
if len(file_attente) == 0:
    print("File vide")

# ============================================================================
# 16. FICHIERS (LECTURE/ÉCRITURE)
# ============================================================================

# Ouvrir et lire un fichier
# Mode 'r' = lecture, 'w' = écriture, 'a' = ajout, 'b' = binaire
# Syntaxe: open(nom_fichier, mode)

# Lire tout le fichier en une chaîne
with open("donnees.txt", "r", encoding="utf-8") as fichier:
    contenu = fichier.read()
    print(contenu)

# Lire ligne par ligne
with open("donnees.txt", "r", encoding="utf-8") as fichier:
    for ligne in fichier:
        print(ligne.strip())  # strip() enlève les \n

# Lire toutes les lignes dans une liste
with open("donnees.txt", "r", encoding="utf-8") as fichier:
    lignes = fichier.readlines()  # Garde les \n
    for ligne in lignes:
        print(ligne)

# Écrire dans un fichier (écrase le contenu)
with open("sortie.txt", "w", encoding="utf-8") as fichier:
    fichier.write("Première ligne\n")
    fichier.write("Deuxième ligne\n")

# Ajouter à la fin d'un fichier (append)
with open("sortie.txt", "a", encoding="utf-8") as fichier:
    fichier.write("Ligne ajoutée\n")

# Écrire plusieurs lignes
lignes_a_ecrire = ["Alice\n", "Bob\n", "Charlie\n"]
with open("noms.txt", "w", encoding="utf-8") as fichier:
    fichier.writelines(lignes_a_ecrire)

# ============================================================================
# 17. MODULES ET IMPORTS
# ============================================================================

# Importer un module entier
import os
print(os.getcwd())  # Affiche le répertoire courant
os.chdir("/chemin/vers/dossier")  # Change de répertoire

# Importer une fonction spécifique
from math import sqrt, pi, sin, cos
print(sqrt(16))      # 4.0
print(pi)            # 3.14159...
print(sin(0))        # 0.0

# Importer tout du module (à éviter généralement)
# from math import *

# Importer avec alias
import numpy as np
from collections import deque as File

# Les modules mathématiques importants
import math
print(math.ceil(3.2))        # 4 (arrondi vers le haut)
print(math.floor(3.8))       # 3 (arrondi vers le bas)
print(math.fabs(-5))         # 5.0 (valeur absolue)
print(math.log(10))          # 2.302... (logarithme naturel)
print(math.log10(100))       # 2.0 (logarithme base 10)
print(math.exp(1))           # 2.718... (e^1)

# Module pour les nombres aléatoires
import random
print(random.randint(1, 10))           # Entier aléatoire entre 1 et 10
print(random.choice([1, 2, 3, 4, 5]))  # Choisit aléatoirement
print(random.random())                 # Float aléatoire entre 0 et 1

# Module datetime pour les dates et heures
import datetime
maintenant = datetime.datetime.now()
print(maintenant)
print(maintenant.year)
print(maintenant.month)
print(maintenant.day)

# Module sys pour les paramètres système
import sys
print(sys.version)                  # Version de Python
print(sys.argv)                     # Arguments de la ligne de commande

# ============================================================================
# 18. FONCTIONS INTÉGRÉES UTILES
# ============================================================================

# len() - longueur
print(len("texte"))         # 5
print(len([1, 2, 3, 4]))    # 4

# min() et max() - valeur minimale et maximale
print(min(5, 2, 8, 1))      # 1
print(max(5, 2, 8, 1))      # 8
print(min([5, 2, 8, 1]))    # 1

# sum() - somme
print(sum([1, 2, 3, 4, 5])) # 15

# abs() - valeur absolue
print(abs(-5))              # 5

# round() - arrondi
print(round(3.7))           # 4
print(round(3.14159, 2))    # 3.14

# sorted() - tri
print(sorted([3, 1, 4, 1, 5]))  # [1, 1, 3, 4, 5]

# reversed() - inverse
print(list(reversed([1, 2, 3])))  # [3, 2, 1]

# all() - vrai si tous les éléments sont vrais
print(all([True, True, True]))      # True
print(all([True, False, True]))     # False

# any() - vrai s'il y a au moins un élément vrai
print(any([False, False, True]))    # True
print(any([False, False, False]))   # False

# zip() - combine les éléments
noms = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for nom, age in zip(noms, ages):
    print(f"{nom}: {age} ans")

# map() - applique une fonction à chaque élément
nombres = [1, 2, 3, 4, 5]
doubles = list(map(lambda x: x * 2, nombres))  # [2, 4, 6, 8, 10]

# filter() - filtre les éléments selon une condition
pairs = list(filter(lambda x: x % 2 == 0, nombres))  # [2, 4]

# ============================================================================
# 19. CHAÎNES DE CARACTÈRES (STRINGS)
# ============================================================================

# Créer des chaînes
texte = "Bonjour le monde"
texte2 = 'Avec des guillemets simples'
texte3 = """Texte sur
plusieurs
lignes"""

# Concaténation
resultat = "Bonjour " + "le " + "monde"  # "Bonjour le monde"
resultat = "Bonjour " * 3                 # "Bonjour Bonjour Bonjour "

# Longueur
taille = len(texte)

# Accéder aux caractères
print(texte[0])     # "B"
print(texte[-1])    # "e"

# Tranches
print(texte[0:7])   # "Bonjour"
print(texte[8:])    # "le monde"

# Méthodes de chaînes
print(texte.lower())            # "bonjour le monde"
print(texte.upper())            # "BONJOUR LE MONDE"
print(texte.capitalize())       # "Bonjour le monde"
print(texte.title())            # "Bonjour Le Monde"
print(texte.replace("monde", "Python"))  # "Bonjour le Python"
print(texte.split(" "))         # ['Bonjour', 'le', 'monde']
print(" ".join(["Bonjour", "le", "monde"]))  # "Bonjour le monde"
print(texte.find("monde"))      # 11 (index du sous-texte)
print(texte.count("o"))         # 2 (nombre d'occurrences)
print(texte.startswith("Bonjour"))  # True
print(texte.endswith("monde"))  # True
print("  texte  ".strip())      # "texte" (enlève les espaces)

# ============================================================================
# 20. COMPRÉHENSIONS DE LISTES (LIST COMPREHENSIONS)
# ============================================================================

# Manière traditionnelle
carrés_traditionnel = []
for i in range(10):
    carrés_traditionnel.append(i ** 2)

# Compréhension de liste (plus pythonique)
carrés = [i ** 2 for i in range(10)]  # [0, 1, 4, 9, 16, ...]

# Avec condition
pairs = [i for i in range(20) if i % 2 == 0]  # [0, 2, 4, 6, ...]

# Avec transformation
mots = ["python", "java", "c"]
mots_majuscules = [mot.upper() for mot in mots]  # ['PYTHON', 'JAVA', 'C']

# Compréhension de dictionnaire
carres_dict = {i: i**2 for i in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Compréhension d'ensemble
uniques = {i % 3 for i in range(10)}  # {0, 1, 2}

# ============================================================================
# 21. GESTION DES ERREURS (TRY/EXCEPT)
# ============================================================================

# Gérer les exceptions
try:
    nombre = int(input("Entrez un nombre: "))
    resultat = 10 / nombre
    print(f"Résultat: {resultat}")
except ValueError:
    print("Erreur: Veuillez entrer un nombre valide")
except ZeroDivisionError:
    print("Erreur: Division par zéro!")
except Exception as e:
    print(f"Erreur inattendue: {e}")
else:
    print("Pas d'erreur")
finally:
    print("Code qui s'exécute toujours")

# ============================================================================
# 22. EXEMPLE PRATIQUE: ALGORITHME DE COMPLEXITÉ
# ============================================================================

# Exemple: Algorithme de tri (Tri à bulles)
def tri_bulles(liste):
    """
    Tri à bulles - Complexité O(n²)
    Compare les éléments adjacents et les échange si besoin
    """
    n = len(liste)
    for i in range(n):
        for j in range(0, n - i - 1):
            if liste[j] > liste[j + 1]:
                # Échange les éléments
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
    return liste

# Utilisation
nombres_non_tries = [64, 34, 25, 12, 22, 11, 90]
print("Avant tri:", nombres_non_tries)
print("Après tri:", tri_bulles(nombres_non_tries.copy()))

# Exemple: Recherche dichotomique (Complexité O(log n))
def recherche_dichotomique(liste, cible):
    """
    Recherche binaire dans une liste triée
    Beaucoup plus rapide que la recherche linéaire
    """
    gauche = 0
    droite = len(liste) - 1
    
    while gauche <= droite:
        milieu = (gauche + droite) // 2
        
        if liste[milieu] == cible:
            return milieu
        elif liste[milieu] < cible:
            gauche = milieu + 1
        else:
            droite = milieu - 1
    
    return -1  # Élément non trouvé

# Utilisation
nombres_tries = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(recherche_dichotomique(nombres_tries, 7))   # 3 (index)
print(recherche_dichotomique(nombres_tries, 20))  # -1 (non trouvé)

# ============================================================================
# 23. CLASSES ET PROGRAMMATION ORIENTÉE OBJET (POO)
# ============================================================================

# Définir une classe
class Personne:
    # Constructeur (initialise l'objet)
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
    
    # Méthode
    def se_presenter(self):
        return f"Je m'appelle {self.nom} et j'ai {self.age} ans"
    
    # Méthode pour modifier l'état
    def vieillir(self):
        self.age += 1

# Créer une instance
personne1 = Personne("Alice", 25)
print(personne1.se_presenter())  # "Je m'appelle Alice et j'ai 25 ans"

personne1.vieillir()
print(personne1.age)  # 26

# ============================================================================
# 24. CONCLUSION ET BONNES PRATIQUES
# ============================================================================

# Commentaires pour documenter le code
# Les commentaires commencent par #

# Pour les commentaires multi-lignes, utilisez """..."""
"""
Ceci est un commentaire multi-ligne
très utile pour documenter les fonctions
et les modules
"""

# Conventions de nommage
# - Variables et fonctions: minuscules avec underscores (snake_case)
# - Classes: PascalCase
# - Constantes: MAJUSCULES

# Indentation: 4 espaces par niveau (OBLIGATOIRE en Python)

# Importer seulement ce dont vous avez besoin
# Évitez: from module import *
# Préférez: from module import fonction1, fonction2

# Utiliser des noms de variables significatifs
# BON: nombre_de_jours = 365
# MAUVAIS: x = 365

# PEP 8: Guide de style Python officiel
# https://www.python.org/dev/peps/pep-0008/

print("\n=== Fin du sommaire de Python ===")