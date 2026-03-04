import matplotlib.pyplot as plt
import numpy as np



aff = plt.subplots(
    figsize=(8, 4),
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

odd_row = np.array([bool(x) for x in [1, 0, 1, 0, 1, 0, 1, 0]])
~odd_row

chess = np.array([[1,0,1,0,1,0,1,0],
                  [0,1,0,1,0,1,0,1],
                  [1,0,1,0,1,0,1,0],
                  [0,1,0,1,0,1,0,1],
                  [1,0,1,0,1,0,1,0],
                  [0,1,0,1,0,1,0,1],
                  [1,0,1,0,1,0,1,0],
                  [0,1,0,1,0,1,0,1]])


plt.figure(figsize=(10,10))
plt.imshow(chess, cmap='gray')
plt.axis(False)

plt.show()