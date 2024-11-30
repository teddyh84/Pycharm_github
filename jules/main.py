import streamlit as st

import jeu_pendu
import jeu_traduction
import Calculatrice
import commentaire

if "menu" not in st.session_state:
    st.session_state.menu = "Accueil"
    st.title("Choisissez un menu à gauche")

st.sidebar.title("🎮 Jeux")
if st.sidebar.button("🪢 Pendu"):
    st.session_state.menu = "Pendu"
if st.sidebar.button("traducteur"):
    st.session_state.menu = "traducteur"
if st.sidebar.button("🧮 Calculatrice"):
    st.session_state.menu = "Calculatrice"

st.sidebar.title("📧 Contact")
if st.sidebar.button("💬 Commentaires"):
    st.session_state.menu = "Commentaires"

# Affichage selon le menu sélectionné
match st.session_state.menu:
    case "Pendu":
        jeu_pendu.main()

    case "Calculatrice":
        Calculatrice.main()

    case "traducteur":
        jeu_traduction.main()

    case "Commentaires":
        commentaire.main()
