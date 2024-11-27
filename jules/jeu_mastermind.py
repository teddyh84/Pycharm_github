import streamlit as st
import random

# Fonction pour générer un code secret
def generate_secret_code(colors, length=4):
    return [random.choice(colors) for _ in range(length)]

# Fonction pour vérifier la proposition
def check_guess(secret, guess):
    # Compte des correspondances exactes et incorrectes
    exact_matches = sum([s == g for s, g in zip(secret, guess)])
    misplaced_matches = sum([min(secret.count(c), guess.count(c)) for c in set(guess)]) - exact_matches
    return exact_matches, misplaced_matches

# Réinitialisation du jeu
def reset_game():
    st.session_state.secret_code = generate_secret_code(colors=["🔴", "🟢", "🔵", "🟡", "🟣", "🟠"])
    st.session_state.attempts = []
    st.session_state.game_over = False
    st.session_state.win = False

def main():
    # Initialisation des variables de session
    if "secret_code" not in st.session_state:
        st.session_state.secret_code = []
        st.session_state.attempts = []
        st.session_state.max_attempts = 10
        st.session_state.game_over = False
        st.session_state.win = False

    # Initialisation du jeu
    if not st.session_state.secret_code:
        reset_game()

    # Interface utilisateur
    st.title("Mastermind 🎯")
    st.write("Devinez la séquence secrète de 4 couleurs parmi : 🔴, 🟢, 🔵, 🟡, 🟣, 🟠.")
    st.write(f"Vous avez **{st.session_state.max_attempts} essais**.")

    # Saisie utilisateur
    if not st.session_state.game_over:
        with st.form("guess_form"):
            guess = st.text_input("Entrez votre proposition (ex: 🔴🔵🟢🟠)", max_chars=8)
            submitted = st.form_submit_button("Valider")

        if submitted:
            # Validation de la saisie
            if len(guess) != 8 or any(c not in "🔴🟢🔵🟡🟣🟠" for c in guess):
                st.error("Veuillez entrer une séquence valide de 4 couleurs (🔴, 🟢, 🔵, 🟡, 🟣, 🟠).")
            else:
                # Convertir l'entrée utilisateur en liste
                user_guess = [guess[i:i+2] for i in range(0, len(guess), 2)]
                st.session_state.attempts.append(user_guess)

                # Vérification de la réponse
                exact, misplaced = check_guess(st.session_state.secret_code, user_guess)
                st.write(f"Votre proposition : {''.join(user_guess)}")
                st.write(f"Exactes : {exact} | Mal placées : {misplaced}")

                # Gagner ou continuer
                if exact == 4:
                    st.session_state.win = True
                    st.session_state.game_over = True
                    st.success("🎉 Félicitations ! Vous avez trouvé la séquence secrète.")
                elif len(st.session_state.attempts) >= st.session_state.max_attempts:
                    st.session_state.game_over = True
                    st.error("💔 Vous avez épuisé vos essais. La séquence était : " + "".join(st.session_state.secret_code))

    # Affichage des tentatives
    if st.session_state.attempts:
        st.write("### Historique des tentatives")
        for i, attempt in enumerate(st.session_state.attempts, 1):
            exact, misplaced = check_guess(st.session_state.secret_code, attempt)
            st.write(f"Essai {i}: {''.join(attempt)} | Exactes : {exact}, Mal placées : {misplaced}")

    # Bouton pour rejouer
    if st.session_state.game_over:
        if st.button("Rejouer"):
            reset_game()
            st.experimental_rerun()
