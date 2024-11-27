import streamlit as st

import jeu_pendu
import commentaire
import formulaire
import onglets

if "menu" not in st.session_state:
    st.session_state.menu = "Accueil"
    st.title("Choisissez un menu à gauche")

st.sidebar.title("🎮 Jeux")
if st.sidebar.button("🪢 Pendu"):
    st.session_state.menu = "Pendu"
st.sidebar.title("📧 Contact")
if st.sidebar.button("💬 Commentaires"):
    st.session_state.menu = "Commentaires"
st.sidebar.title("Exemples")
if st.sidebar.button("Page avec onglets"):
    st.session_state.menu = "Onglets"
if st.sidebar.button("Exemple de formulaire"):
    st.session_state.menu = "Formulaire"

# Affichage selon le menu sélectionné
match st.session_state.menu:
    case "Pendu":
        jeu_pendu.main()

    case "Commentaires":
        commentaire.main()

    case "Onglets":
        onglets.main()

    case "Formulaire":
        formulaire.main()