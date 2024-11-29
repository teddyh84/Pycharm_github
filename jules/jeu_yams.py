import streamlit as st
import random

# Réinitialiser le jeu
def reset_game():
    st.session_state.dice = [0, 0, 0, 0, 0]
    st.session_state.rolls_left = 3
    st.session_state.held_dice = [False, False, False, False, False]
    st.session_state.scores = []
    st.session_state.game_over = False

# Fonction pour lancer les dés
def roll_dice():
    if st.session_state.rolls_left > 0:
        for i in range(5):
            if not st.session_state.held_dice[i]:  # Ne pas lancer les dés bloqués
                st.session_state.dice[i] = random.randint(1, 6)
        st.session_state.rolls_left -= 1

# Calcul du score pour un chiffre donné
def calculate_score(number):
    return sum(d for d in st.session_state.dice if d == number)

def main():
    # Interface principale
    st.title("🎲 Jeu de Yams (Yahtzee) 🎲")

    # Initialisation des variables de session
    if "dice" not in st.session_state:
        st.session_state.dice = [0, 0, 0, 0, 0]  # Les 5 dés
        st.session_state.rolls_left = 3  # Nombre de lancers restants
        st.session_state.held_dice = [False, False, False, False, False]  # Dés bloqués
        st.session_state.scores = []  # Tableau des scores
        st.session_state.game_over = False

    # Lancer les dés
    if not st.session_state.game_over:
        st.write(f"Vous avez **{st.session_state.rolls_left} lancers** restants.")
        if st.button("Lancer les dés"):
            roll_dice()

        # Afficher les dés
        st.write("### Vos dés :")
        cols = st.columns(5)
        for i, col in enumerate(cols):
            with col:
                st.write(f"🎲 {st.session_state.dice[i]}")
                if st.session_state.rolls_left > 0:
                    st.session_state.held_dice[i] = st.checkbox("Bloquer", key=f"hold_{i}")

        # Calculer le score
        st.write("### Sélectionnez une catégorie pour marquer des points :")
        cols = st.columns(6)
        for i in range(1, 7):
            with cols[i - 1]:
                if st.button(f"{i} ({calculate_score(i)} points)", key=f"score_{i}"):
                    st.session_state.scores.append(calculate_score(i))
                    st.session_state.rolls_left = 3
                    st.session_state.held_dice = [False, False, False, False, False]
                    st.session_state.dice = [0, 0, 0, 0, 0]
                    if len(st.session_state.scores) == 6:  # Fin du jeu après 6 catégories
                        st.session_state.game_over = True

    # Afficher le tableau des scores
    if st.session_state.scores:
        st.write("### Tableau des Scores :")
        total_score = sum(st.session_state.scores)
        for i, score in enumerate(st.session_state.scores, start=1):
            st.write(f"Catégorie {i} : {score} points")
        st.write(f"**Score total : {total_score} points**")

    # Fin du jeu
    if st.session_state.game_over:
        st.success("🎉 Jeu terminé !")
        st.write(f"Votre score final est : **{sum(st.session_state.scores)} points**")
        if st.button("Rejouer"):
            reset_game()
