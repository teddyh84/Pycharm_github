import streamlit as st
import numpy as np
import random

# Initialisation de la grille
def initialize_grid():
    grid = np.zeros((4, 4), dtype=int)
    add_new_tile(grid)
    add_new_tile(grid)
    return grid

# Ajouter une nouvelle tuile (2 ou 4) à un emplacement vide
def add_new_tile(grid):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if grid[i, j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        grid[i, j] = 2 if random.random() < 0.9 else 4

# Déplacer les tuiles dans une direction
def move(grid, direction):
    def merge(row):
        non_zero = row[row != 0]
        merged = []
        skip = False
        for i in range(len(non_zero)):
            if skip:
                skip = False
                continue
            if i < len(non_zero) - 1 and non_zero[i] == non_zero[i + 1]:
                merged.append(non_zero[i] * 2)
                skip = True
            else:
                merged.append(non_zero[i])
        return np.array(merged + [0] * (len(row) - len(merged)))

    if direction == "gauche":
        grid = np.array([merge(row) for row in grid])
    elif direction == "droite":
        grid = np.array([merge(row[::-1])[::-1] for row in grid])
    elif direction == "haut":
        grid = np.array([merge(col) for col in grid.T]).T
    elif direction == "bas":
        grid = np.array([merge(col[::-1])[::-1] for col in grid.T]).T

    return grid

# Vérifie si le joueur a perdu
def check_game_over(grid):
    if any(0 in row for row in grid):
        return False
    for i in range(4):
        for j in range(4):
            if (i > 0 and grid[i, j] == grid[i - 1, j]) or \
               (j > 0 and grid[i, j] == grid[i, j - 1]):
                return False
    return True

# Streamlit App
st.title("2048 avec Streamlit")
st.markdown("Utilisez les boutons pour déplacer les tuiles dans la grille.")

# Initialisation ou récupération de la grille
if "grid" not in st.session_state:
    st.session_state.grid = initialize_grid()

grid = st.session_state.grid

# Affichage de la grille
st.write("### Grille actuelle :")
for row in grid:
    st.text(" ".join(f"{val:4}" if val != 0 else "    " for val in row))

# Boutons pour déplacer
col1, col2, col3, col4 = st.columns(4)
if col1.button("⬅️ Gauche"):
    new_grid = move(grid, "gauche")
elif col2.button("⬆️ Haut"):
    new_grid = move(grid, "haut")
elif col3.button("⬇️ Bas"):
    new_grid = move(grid, "bas")
elif col4.button("➡️ Droite"):
    new_grid = move(grid, "droite")
else:
    new_grid = grid

# Ajout d'une nouvelle tuile si le mouvement est valide
if not np.array_equal(grid, new_grid):
    add_new_tile(new_grid)
    st.session_state.grid = new_grid

# Vérification de fin de partie
if check_game_over(new_grid):
    st.error("Game Over! Vous avez perdu.")
else:
    st.success("Continuez à jouer !")

