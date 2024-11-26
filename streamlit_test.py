import streamlit as st
import pygame

# Titre de l'application
st.title("Additionneur Simple")

# Instructions pour l'utilisateur
st.write("Entrez deux nombres et cliquez sur le bouton pour obtenir la somme.")

# Champs de saisie pour les deux nombres
num1 = st.number_input("Entrez le premier nombre :", value=0)
num2 = st.number_input("Entrez le deuxième nombre :", value=0)

# Bouton pour déclencher l'addition
if st.button("Calculer la somme"):
    somme = num1 + num2
    st.success(f"La somme de {num1} et {num2} est {somme}.")
else:
    st.warning(f"ah bah boaw")





# Initialisation
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mon Premier Jeu")
clock = pygame.time.Clock()

# Couleurs
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Boucle principale
running = True
while running:
    screen.fill(WHITE)

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Dessin d'un rectangle
    pygame.draw.rect(screen, RED, (100, 100, 200, 100))

    # Mise à jour de l'écran
    pygame.display.flip()
    clock.tick(60)

pygame.quit()


