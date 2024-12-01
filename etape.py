import streamlit as st

# Initialisation de l'état de l'étape
if "step" not in st.session_state:
    st.session_state.step = 1


# Fonction pour gérer les clics de bouton
def handle_button(action):
    if action == "next":
        st.session_state.step += 1
    elif action == "previous":
        st.session_state.step -= 1
    elif action == "reset":
        st.session_state.step = 1


# Étape 1
if st.session_state.step == 1:
    st.title("Étape 1 : Introduction")
    st.write("Bienvenue ! Cliquez sur Suivant pour continuer.")
    if st.button("Suivant"):
        handle_button("next")

# Étape 2
elif st.session_state.step == 2:
    st.title("Étape 2 : Formulaire")
    name = st.text_input("Votre nom", key="name_input")
    age = st.number_input("Votre âge", min_value=0, max_value=120, key="age_input")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Précédent"):
            handle_button("previous")
    with col2:
        if st.button("Suivant"):
            handle_button("next")

# Étape 3
elif st.session_state.step == 3:
    st.title("Étape 3 : Confirmation")
    st.write(f"Nom : {st.session_state.get('name_input', 'Non renseigné')}")
    st.write(f"Âge : {st.session_state.get('age_input', 'Non renseigné')} ans")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Précédent"):
            handle_button("previous")
    with col2:
        if st.button("Terminer"):
            handle_button("reset")
            st.write("Merci pour votre participation !")

