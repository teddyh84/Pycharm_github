import streamlit as st
import numpy as np
import time
from PIL import Image, ImageDraw

# Configuration de la grille du jeu
GRID_SIZE = 20  # Taille de la grille (20x20)
CELL_SIZE = 20  # Taille d'une cellule (en pixels)

# Initialisation du serpent et de la nourriture
def initialize_game():
    snake = [(5, 5), (5, 4), (5, 3)]  # Le serpent commence avec 3 segments
    direction = "RIGHT"  # Direction initiale
    food = (np.random.randint(0, GRID_SIZE), np.random.randint(0, GRID_SIZE))  # Nourriture aléatoire
    return snake, direction, food

# Dessine le plateau de jeu
def draw_game(snake, food):
    img = Image.new("RGB", (GRID_SIZE * CELL_SIZE, GRID_SIZE * CELL_SIZE), "black")
    draw = ImageDraw.Draw(img)

    # Dessiner la nourriture
    fx, fy = food
    draw.rectangle(
        [fx * CELL_SIZE, fy * CELL_SIZE, (fx + 1) * CELL_SIZE, (fy + 1) * CELL_SIZE],
        fill="red",
    )

    # Dessiner le serpent
    for x, y in snake:
        draw.rectangle(
            [x * CELL_SIZE, y * CELL_SIZE, (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE],
            fill="green",
        )

    return img

# Met à jour la position du serpent
def move_snake(snake, direction):
    head_x, head_y = snake[0]
    if direction == "UP":
        head_y -= 1
    elif direction == "DOWN":
        head_y += 1
    elif direction == "LEFT":
        head_x -= 1
    elif direction == "RIGHT":
        head_x += 1

    new_head = (head_x, head_y)
    snake = [new_head] + snake[:-1]
    return snake

# Vérifie si le serpent mange la nourriture
def check_food(snake, food):
    if snake[0] == food:
        snake.append(snake[-1])  # Ajoute un segment au serpent
        food = (np.random.randint(0, GRID_SIZE), np.random.randint(0, GRID_SIZE))
    return snake, food

# Vérifie si le jeu est terminé
def check_collision(snake):
    head = snake[0]
    # Collision avec les murs
    if head[0] < 0 or head[0] >= GRID_SIZE or head[1] < 0 or head[1] >= GRID_SIZE:
        return True
    # Collision avec soi-même
    if head in snake[1:]:
        return True
    return False

# Initialisation du jeu
if "snake" not in st.session_state:
    st.session_state.snake, st.session_state.direction, st.session_state.food = initialize_game()
    st.session_state.game_over = False

# Affichage du jeu
st.title("Jeu du Serpent")
st.write("Utilisez les boutons pour contrôler le serpent !")

col1, col2, col3 = st.columns(3)
if col1.button("⬅️ Gauche"):
    if st.session_state.direction != "RIGHT":  # Empêche de revenir dans l'autre sens
        st.session_state.direction = "LEFT"
if col2.button("⬆️ Haut"):
    if st.session_state.direction != "DOWN":
        st.session_state.direction = "UP"
if col3.button("➡️ Droite"):
    if st.session_state.direction != "LEFT":
        st.session_state.direction = "RIGHT"
if st.button("⬇️ Bas"):
    if st.session_state.direction != "UP":
        st.session_state.direction = "DOWN"

# Logique du jeu
if not st.session_state.game_over:
    st.session_state.snake = move_snake(st.session_state.snake, st.session_state.direction)
    st.session_state.snake, st.session_state.food = check_food(st.session_state.snake, st.session_state.food)
    st.session_state.game_over = check_collision(st.session_state.snake)

# Afficher l'état du jeu
game_image = draw_game(st.session_state.snake, st.session_state.food)
st.image(game_image, caption="Jeu du Serpent", use_column_width=True)

# Afficher le message de fin
if st.session_state.game_over:
    st.error("Game Over! Cliquez sur 'Rafraîchir' pour recommencer.")
