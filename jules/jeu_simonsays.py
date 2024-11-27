import streamlit as st
import random
import time

# Fonction pour générer une séquence aléatoire
def generate_sequence(sequence, round):
    colors = ["🔴", "🟢", "🔵", "🟡"]
    for _ in range(round):
        sequence.append(random.choice(colors))
    return sequence

# Fonction pour afficher la séquence avec un délai
def display_sequence(sequence):
    st.write("### Regardez la séquence :")
    for color in sequence:
        st.markdown(f"<div style='font-size: 50px; text-align: center;'>{color}</div>", unsafe_allow_html=True)
        time.sleep(1)
        st.write("")  # Efface l'écran temporairement
        time.sleep(0.5)

# Réinitialiser le jeu
def reset_game():
    st.session_state.sequence = []
    st.session_state.user_sequence = []
    st.session_state.round = 1
    st.session_state.game_over = False



def main():
    # Initialiser la session si nécessaire
    if "sequence" not in st.session_state:
        st.session_state.sequence = []  # Séquence générée par le jeu
        st.session_state.user_sequence = []  # Séquence entrée par l'utilisateur
        st.session_state.round = 1  # Niveau du jeu
        st.session_state.game_over = False


    # Interface principale
    st.title("Simon Says 🟢🔴🔵🟡")

    if st.session_state.game_over:
        st.error("Game Over ! 😢 Essayez encore !")
        if st.button("Rejouer"):
            reset_game()

    # Nouveau round
    if not st.session_state.game_over:
        st.write(f"### Round {st.session_state.round}")
        if st.button("Commencer la Séquence"):
            # Générer et afficher la séquence
            st.session_state.sequence = generate_sequence(st.session_state.sequence, st.session_state.round)
            display_sequence(st.session_state.sequence)
            st.session_state.user_sequence = []  # Réinitialiser les réponses utilisateur

        # Boutons pour les couleurs
        st.write("### Reproduisez la Séquence :")
        cols = st.columns(4)
        color_map = {"🔴": 0, "🟢": 1, "🔵": 2, "🟡": 3}

        for color, col in zip(color_map.keys(), cols):
            if col.button(color):
                st.session_state.user_sequence.append(color)

        # Vérification de la séquence
        if len(st.session_state.user_sequence) == len(st.session_state.sequence):
            if st.session_state.user_sequence == st.session_state.sequence:
                st.success("Bien joué ! Passons au round suivant 🎉")
                st.session_state.round += 1
                st.session_state.user_sequence = []
            else:
                st.session_state.game_over = True
                st.error("Mauvaise séquence ! 😢")

