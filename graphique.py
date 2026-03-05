import matplotlib.pyplot as plt
import numpy as np

taille = int(input("quelle taille ? : "))

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
aff.invert_yaxis() # remettre les chiffres de droite a l'envers.

# Réglages de l'axe

plt.show()